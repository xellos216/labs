# Ubuntu Server VM Installation and Maintenance Runbook

## Metadata

```yaml
Roadmap: Linux Server Administration
Phase: 00
DocumentType: Operational Runbook
Title: Ubuntu Server VM Installation and Maintenance
Status: Active
ArchiveVersion: 3
Date: 2026-07-11
HostOS: Arch Linux
GuestOS: Ubuntu Server 26.04 LTS
Hypervisor: QEMU/KVM
ManagementLayer: libvirt
```

---

## Purpose

This document records the installation, validation, operation, maintenance, and
recovery workflow for the primary Ubuntu Server laboratory VM.

It is intended to answer the following operational questions:

- How is the VM installed from an ISO?
- How are libvirt networking and storage configured?
- How is Host firewall interference diagnosed?
- How is SSH key-only administration configured?
- How is the VM started and stopped safely?
- How is the known-good state preserved and restored?
- What should be checked during routine maintenance?

This is an operational runbook, not an additional numbered roadmap session.

---

## Final Architecture

```text
Physical CPU
↓
Arch Linux Host
↓
libvirt
├─ QEMU
├─ KVM
├─ default storage pool
└─ default NAT network
   ├─ virbr0
   ├─ dnsmasq DHCP/DNS
   └─ IPv4 masquerading
↓
Ubuntu Server Guest
├─ virtio disk
├─ virtio NIC
├─ LVM root filesystem
├─ OpenSSH
└─ key-only remote administration
```

---

## Known-Good Baseline

```text
VM name:
ubuntu-server-lab

Guest OS:
Ubuntu Server 26.04 LTS

Firmware:
UEFI
Secure Boot disabled

Virtual CPUs:
4

Memory:
8 GiB

Virtual disk:
60 GiB qcow2

Disk location:
/var/lib/libvirt/images/ubuntu-server-lab.qcow2

Virtual network:
libvirt default NAT

Virtual subnet:
192.168.122.0/24

Guest administration:
SSH public-key authentication

Password authentication over SSH:
disabled

Baseline snapshot:
baseline-initial
```

The VM does not require a graphical console login before SSH can be used.

```text
VM boots
↓
network is configured
↓
ssh.socket listens on TCP 22
↓
Host connects through SSH
```

---

## Host Requirements

### Hardware virtualization

Check CPU virtualization support and KVM access:

```bash
lscpu | grep -E 'Virtualization|Hypervisor' || true
lsmod | grep -E '^(kvm|kvm_intel|kvm_amd|vhost_net)' || true
ls -l /dev/kvm
```

Validate the complete QEMU/KVM Host environment:

```bash
sudo virt-host-validate qemu
```

Expected important results:

```text
hardware virtualization: PASS
/dev/kvm exists: PASS
/dev/kvm accessible: PASS
/dev/vhost-net exists: PASS
/dev/net/tun exists: PASS
cgroup controllers: PASS
IOMMU support: PASS
```

Secure Guest warnings related to SEV or TDX do not prevent a normal Ubuntu
Server VM from operating.

---

## Host Package Installation

The initial laboratory installation used:

```bash
sudo pacman -Syu \
  qemu-full \
  libvirt \
  virt-manager \
  virt-viewer \
  dnsmasq \
  edk2-ovmf \
  swtpm
```

After a kernel, systemd, or core library upgrade, reboot the Host before
continuing:

```bash
sudo reboot
```

Verify the tools:

```bash
command -v qemu-system-x86_64
command -v virsh
command -v virt-manager
command -v virt-viewer
```

---

## libvirt Service Setup

Enable the libvirt management and logging services:

```bash
sudo systemctl enable --now libvirtd virtlogd
```

Verify:

```bash
systemctl is-enabled libvirtd virtlogd
systemctl is-active libvirtd virtlogd
```

Test the system-level libvirt connection:

```bash
virsh -c qemu:///system version
```

The connection path is:

```text
virsh
↓
qemu:///system
↓
system libvirt daemon
↓
QEMU/KVM virtual machines
```

The `virsh` command belongs on the Arch Host. It is not normally installed or
needed inside the Ubuntu Guest.

---

## libvirt Default Network

Inspect existing networks:

```bash
virsh -c qemu:///system net-list --all
```

Start and enable the default network:

```bash
sudo virsh -c qemu:///system net-start default
sudo virsh -c qemu:///system net-autostart default
```

Verify:

```bash
virsh -c qemu:///system net-list --all
ip -brief address show virbr0
virsh -c qemu:///system net-dumpxml default
```

Expected model:

```text
Host virtual bridge:
virbr0

Host-side gateway:
192.168.122.1/24

Guest DHCP range:
192.168.122.2–192.168.122.254
```

Before a VM NIC is connected, `virbr0` may exist without an active lower-layer
carrier. After the VM starts, its Host-side `vnet` interface should join the
bridge.

Inspect the running path:

```bash
ip -brief link show virbr0
bridge link show master virbr0
virsh -c qemu:///system domiflist ubuntu-server-lab
```

---

## libvirt Storage Pool

The VM image directory is:

```text
/var/lib/libvirt/images
```

Inspect available Host storage:

```bash
df -h /var/lib/libvirt
sudo ls -ld /var/lib/libvirt/images
```

Define the directory as the default storage pool:

```bash
virsh -c qemu:///system pool-define-as \
  --name default \
  --type dir \
  --target /var/lib/libvirt/images
```

Start it and enable automatic startup:

```bash
virsh -c qemu:///system pool-start default
virsh -c qemu:///system pool-autostart default
```

Verify:

```bash
virsh -c qemu:///system pool-list --all
virsh -c qemu:///system pool-info default
virsh -c qemu:///system pool-dumpxml default
```

Expected state:

```text
State: running
Persistent: yes
Autostart: yes
Path: /var/lib/libvirt/images
```

---

## Installation ISO

Create a local ISO directory:

```bash
mkdir -p ~/Downloads/iso
cd ~/Downloads/iso
```

Download the selected Ubuntu Server ISO from the official Ubuntu release
server:

```bash
curl --fail \
  --location \
  --continue-at - \
  --output ubuntu-server.iso \
  '<OFFICIAL_ISO_URL>'
```

Verify the ISO against the checksum published for that exact image:

```bash
echo '<OFFICIAL_SHA256>  ubuntu-server.iso' |
  sha256sum --check
```

Do not continue unless the result is:

```text
ubuntu-server.iso: OK
```

Inspect the image:

```bash
ls -lh ubuntu-server.iso
file ubuntu-server.iso
```

Copy the ISO into the libvirt storage pool:

```bash
sudo install -m 0644 \
  ~/Downloads/iso/ubuntu-server.iso \
  /var/lib/libvirt/images/ubuntu-server.iso
```

Refresh and inspect the pool:

```bash
virsh -c qemu:///system pool-refresh default
virsh -c qemu:///system vol-list default
```

---

## VM Resource Selection

The Host used for this lab had sufficient CPU and memory for the following
allocation:

```text
vCPU: 4
RAM: 8 GiB
Disk: 60 GiB
```

Inspect Host resources before using these values elsewhere:

```bash
lscpu | grep -E 'Model name|Socket|Core|Thread|^CPU\(s\)'
nproc
free -h
uptime
df -h /var/lib/libvirt/images
```

Avoid allocating resources based only on the VM workload. Preserve enough CPU,
memory, and storage for the Host to remain responsive.

---

## VM Definition Dry Run

Before creating the VM, generate its XML without making changes:

```bash
virt-install \
  --connect qemu:///system \
  --name ubuntu-server-lab \
  --memory 8192 \
  --vcpus 4,sockets=1,cores=4,threads=1 \
  --cpu host-model \
  --machine q35 \
  --boot uefi,firmware.feature0.name=secure-boot,firmware.feature0.enabled=no \
  --osinfo ubuntu24.04 \
  --disk pool=default,size=60,format=qcow2,bus=virtio \
  --network network=default,model=virtio \
  --graphics spice \
  --cdrom /var/lib/libvirt/images/ubuntu-server.iso \
  --dry-run \
  --print-xml \
  > /tmp/ubuntu-server-lab.xml
```

At installation time, the local `osinfo-db` did not yet provide an Ubuntu 26.04
profile. The Ubuntu 24.04 profile was used only as a virtual hardware profile;
the ISO still installed Ubuntu 26.04.

Inspect important fields:

```bash
grep -E \
  '<name>|<memory|<vcpu|<type arch|firmware=|secure-boot|source file=|source network=|model type=|<graphics' \
  /tmp/ubuntu-server-lab.xml
```

Confirm that the dry run created nothing:

```bash
virsh -c qemu:///system list --all

sudo test -e /var/lib/libvirt/images/ubuntu-server-lab.qcow2 &&
  echo "unexpected disk exists" ||
  echo "VM disk not created: expected"
```

---

## VM Creation

Create and start the VM:

```bash
virt-install \
  --connect qemu:///system \
  --name ubuntu-server-lab \
  --memory 8192 \
  --vcpus 4,sockets=1,cores=4,threads=1 \
  --cpu host-model \
  --machine q35 \
  --boot uefi,firmware.feature0.name=secure-boot,firmware.feature0.enabled=no \
  --osinfo ubuntu24.04 \
  --disk pool=default,size=60,format=qcow2,bus=virtio \
  --network network=default,model=virtio \
  --graphics spice \
  --cdrom /var/lib/libvirt/images/ubuntu-server.iso \
  --noautoconsole
```

Verify:

```bash
virsh -c qemu:///system list --all
virsh -c qemu:///system domiflist ubuntu-server-lab
sudo ls -lh /var/lib/libvirt/images/ubuntu-server-lab.qcow2
```

The qcow2 file may display its virtual size with `ls`. Use `du` and
`qemu-img info` to inspect actual allocation:

```bash
sudo du -h /var/lib/libvirt/images/ubuntu-server-lab.qcow2
sudo qemu-img info /var/lib/libvirt/images/ubuntu-server-lab.qcow2
```

---

## Installer Console

Open the graphical console:

```bash
virt-viewer \
  --connect qemu:///system \
  --zoom=180 \
  --cursor=local \
  --hotkeys=release-cursor=ctrl+alt,toggle-fullscreen=shift+f11 \
  ubuntu-server-lab
```

Console controls:

```text
Release captured keyboard and pointer:
Ctrl+Alt

Toggle fullscreen:
Shift+F11
```

Closing `virt-viewer` does not stop the VM. It closes only the console client.

---

## Ubuntu Installer Choices

The installation used the following choices:

```text
Language:
English

Installation type:
Ubuntu Server

Minimized installation:
No

Third-party drivers:
No

Network:
Automatic DHCP

Proxy:
None

Archive mirror:
Default Ubuntu archive

Storage:
Use entire virtual disk

LVM:
Enabled

LUKS encryption:
Disabled

Ubuntu Pro:
Skipped

OpenSSH server:
Installed

Password authentication during installation:
Temporarily enabled

Imported SSH identity:
None

Featured Server Snaps:
None
```

Suggested identity values for a public lab example:

```text
Display name:
Lab User

Hostname:
ubuntu-server-lab

Username:
labuser
```

Do not record passwords in the repository.

---

## Guest Storage Layout

The guided LVM installation created a structure similar to:

```text
/dev/vda
├─ EFI System Partition
│  └─ /boot/efi
├─ ext4 boot partition
│  └─ /boot
└─ LVM physical volume
   └─ ubuntu-vg
      ├─ ubuntu-lv
      │  └─ /
      └─ unallocated volume-group space
```

The installer intentionally left part of the volume group unused. This space
can later support:

- root logical volume expansion
- a separate `/srv` logical volume
- a separate `/var` logical volume
- LVM extension and recovery exercises

Inspect from inside the Guest:

```bash
lsblk -f
findmnt /
sudo pvs
sudo vgs
sudo lvs
```

---

## Installation Media Removal

After installation completes, eject the ISO from both the live and persistent
VM configuration:

```bash
virsh -c qemu:///system change-media \
  ubuntu-server-lab \
  sda \
  --eject \
  --live \
  --config
```

Verify:

```bash
virsh -c qemu:///system domblklist \
  ubuntu-server-lab \
  --details

virsh -c qemu:///system domblklist \
  ubuntu-server-lab \
  --inactive \
  --details
```

Expected CD-ROM source:

```text
file   cdrom   sda   -
```

If the ISO is removed before installation finishes, reinsert it while the VM
is shut down:

```bash
virsh -c qemu:///system change-media \
  ubuntu-server-lab \
  sda \
  --insert \
  /var/lib/libvirt/images/ubuntu-server.iso \
  --config
```

---

## Host Firewall Compatibility

### Observed failure

The Guest sent DHCP Discover packets, but no DHCP Offer returned.

Packet path:

```text
Guest NIC
↓
Host vnet interface
↓
virbr0
↓
UFW INPUT policy
↓
packet dropped before dnsmasq
```

The Host was also configured with a default routed-traffic deny policy. After
DHCP succeeded, Guest traffic reached the Host but was dropped before reaching
libvirt NAT masquerading.

Observed second failure:

```text
Guest
↓
virbr0
↓
libvirt forwarding rule accepted
↓
UFW FORWARD policy dropped
↓
libvirt NAT counter remained zero
```

### DHCP observation

Capture DHCP traffic on the Host:

```bash
sudo tcpdump -ni virbr0 -e -vv \
  'udp port 67 or udp port 68'
```

Expected exchange:

```text
DHCP Discover
DHCP Offer
DHCP Request
DHCP ACK
```

### Permanent DHCP and DNS rules

Back up the UFW configuration:

```bash
sudo cp -a \
  /etc/ufw/before.rules \
  "/etc/ufw/before.rules.bak-$(date +%Y%m%d-%H%M%S)"
```

Inside the `*filter` section of `/etc/ufw/before.rules`, before its `COMMIT`
line, add:

```text
# libvirt default NAT bridge: DHCP and DNS to host
-A ufw-before-input -i virbr0 -p udp --dport 67 -j ACCEPT
-A ufw-before-input -i virbr0 -p udp --dport 53 -j ACCEPT
-A ufw-before-input -i virbr0 -p tcp --dport 53 -j ACCEPT
```

Apply the rules:

```bash
sudo ufw reload
```

Verify:

```bash
sudo iptables -vnL ufw-before-input --line-numbers
virsh -c qemu:///system net-dhcp-leases default
```

These rules permit only DHCP and DNS traffic arriving through the libvirt
bridge.

### Permanent routed-traffic rule

Permit outbound forwarding from the libvirt subnet:

```bash
sudo ufw route allow \
  in on virbr0 \
  from 192.168.122.0/24 \
  to any \
  comment 'libvirt default NAT outbound'
```

Verify:

```bash
sudo ufw status numbered
sudo iptables -vnL ufw-user-forward --line-numbers
```

This rule permits Guest-originated routed traffic. It does not create an
arbitrary inbound connection from the external network to the Guest.

### Forwarding and NAT diagnostics

```bash
sysctl net.ipv4.ip_forward
sudo iptables -vnL FORWARD --line-numbers
sudo iptables -t nat -vnL POSTROUTING --line-numbers
sudo nft -a list table ip libvirt_network
```

Expected:

```text
net.ipv4.ip_forward = 1
Guest traffic accepted from virbr0
Return traffic accepted as established or related
192.168.122.0/24 traffic masqueraded toward external networks
```

---

## Initial Guest Validation

After the first disk boot, inspect the Guest:

```bash
echo "## identity"
whoami
hostnamectl

echo
echo "## network"
ip -brief address
ip route

echo
echo "## SSH"
systemctl is-enabled ssh.service ssh.socket 2>&1
systemctl is-active ssh.service ssh.socket 2>&1
ss -lntp | grep ':22'

echo
echo "## storage"
lsblk -f
findmnt /
```

A valid initial state includes:

```text
hostname:
ubuntu-server-lab

network:
Guest address from 192.168.122.0/24

default route:
via 192.168.122.1

SSH:
ssh.socket enabled
ssh.socket active
TCP 22 listening

root filesystem:
ext4 on an LVM logical volume
```

On the observed Ubuntu installation, `ssh.service` was active while
`ssh.socket` was enabled. A disabled `ssh.service` does not necessarily mean
SSH will fail after reboot when socket activation is enabled.

---

## SSH Host-Key Verification

Inside the Guest, display the ED25519 host-key fingerprint:

```bash
sudo ssh-keygen -lf /etc/ssh/ssh_host_ed25519_key.pub
```

On the Host, connect:

```bash
ssh labuser@<VM_IP>
```

Compare the displayed fingerprint with the value read directly from the Guest
console before accepting it.

Only accept the host key when the fingerprints match.

---

## SSH Public-Key Installation

Inspect Host public keys:

```bash
find ~/.ssh \
  -maxdepth 1 \
  -type f \
  -name '*.pub' \
  -print \
  -exec ssh-keygen -lf {} \;
```

Install the selected public key:

```bash
ssh-copy-id \
  -i ~/.ssh/id_ed25519.pub \
  labuser@<VM_IP>
```

Test public-key-only authentication:

```bash
ssh \
  -o PreferredAuthentications=publickey \
  -o PasswordAuthentication=no \
  labuser@<VM_IP>
```

Expected:

```text
labuser@ubuntu-server-lab:~$
```

---

## SSH Hardening

Keep one verified SSH session open while modifying authentication settings.

Inspect effective settings inside the Guest:

```bash
sudo sshd -T |
  grep -E \
  '^(pubkeyauthentication|passwordauthentication|kbdinteractiveauthentication|permitrootlogin) '
```

Inspect configuration sources:

```bash
sudo grep -RnsE \
  '^[[:space:]]*(Include|PubkeyAuthentication|PasswordAuthentication|KbdInteractiveAuthentication|PermitRootLogin)' \
  /etc/ssh/sshd_config \
  /etc/ssh/sshd_config.d \
  2>/dev/null
```

The installer may create:

```text
/etc/ssh/sshd_config.d/50-cloud-init.conf
```

Create an earlier local drop-in:

```bash
sudo tee /etc/ssh/sshd_config.d/00-local-hardening.conf >/dev/null <<'EOF'
PubkeyAuthentication yes
PasswordAuthentication no
KbdInteractiveAuthentication no
EOF
```

Set permissions:

```bash
sudo chmod 0644 \
  /etc/ssh/sshd_config.d/00-local-hardening.conf
```

Validate syntax and effective behavior:

```bash
sudo sshd -t &&
  echo "sshd configuration: valid"

sudo sshd -T |
  grep -E \
  '^(pubkeyauthentication|passwordauthentication|kbdinteractiveauthentication|permitrootlogin) '
```

Expected:

```text
pubkeyauthentication yes
passwordauthentication no
kbdinteractiveauthentication no
permitrootlogin prohibit-password
```

Reload without dropping the established connection:

```bash
sudo systemctl reload ssh.service
```

Verify public-key access from a second Host terminal:

```bash
ssh \
  -o BatchMode=yes \
  -o PreferredAuthentications=publickey \
  -o PasswordAuthentication=no \
  labuser@<VM_IP>
```

Verify password authentication is rejected:

```bash
ssh \
  -o PubkeyAuthentication=no \
  -o PreferredAuthentications=password \
  -o KbdInteractiveAuthentication=no \
  labuser@<VM_IP>
```

Expected:

```text
Permission denied (publickey).
```

Do not close the original administrative session until the second public-key
test succeeds.

---

## Guest Package Updates

Refresh package metadata:

```bash
sudo apt update
```

Inspect pending changes:

```bash
apt list --upgradable 2>/dev/null
```

Apply updates:

```bash
sudo apt full-upgrade
```

Inspect the resulting state:

```bash
apt list --upgradable 2>/dev/null

if test -f /var/run/reboot-required; then
  cat /var/run/reboot-required
  cat /var/run/reboot-required.pkgs 2>/dev/null || true
else
  echo "reboot not required"
fi

systemctl --failed
```

Some packages may be deferred due to phased rollout:

```bash
sudo apt-get --simulate full-upgrade
```

A result such as the following is not an error:

```text
The following upgrades have been deferred due to phasing
```

Do not force phased updates unless there is a specific operational reason.

---

## Post-Update Reboot Validation

Reboot the Guest:

```bash
sudo reboot
```

From the Host, wait for it to return:

```bash
watch -t -n 1 \
  'virsh -c qemu:///system domstate ubuntu-server-lab'
```

Connect with public-key authentication only:

```bash
ssh \
  -o BatchMode=yes \
  -o PreferredAuthentications=publickey \
  -o PasswordAuthentication=no \
  labuser@<VM_IP>
```

Inside the Guest:

```bash
echo "## system"
hostname
uname -r
uptime -s

echo
echo "## network"
ip -brief address
ip route

echo
echo "## SSH"
systemctl is-enabled ssh.socket
systemctl is-active ssh.socket ssh.service

sudo sshd -T |
  grep -E \
  '^(pubkeyauthentication|passwordauthentication|kbdinteractiveauthentication) '

echo
echo "## failed services"
systemctl --failed
```

Expected:

```text
Guest boots from qcow2 disk
DHCP address is present
default route is present
ssh.socket is enabled and active
public-key authentication is enabled
password authentication is disabled
no failed systemd units
```

---

## Baseline Snapshot

Shut down the Guest cleanly:

```bash
sudo poweroff
```

Confirm the VM is off from the Host:

```bash
virsh -c qemu:///system domstate ubuntu-server-lab
```

Create the known-good snapshot:

```bash
virsh -c qemu:///system snapshot-create-as \
  ubuntu-server-lab \
  baseline-initial \
  "Ubuntu installed, updated, network verified, SSH key-only" \
  --atomic \
  --validate
```

Verify:

```bash
virsh -c qemu:///system snapshot-list \
  ubuntu-server-lab \
  --tree

virsh -c qemu:///system snapshot-current \
  ubuntu-server-lab \
  --name
```

Expected current snapshot:

```text
baseline-initial
```

A snapshot supports rapid rollback but is not a substitute for an independent
backup of important data.

---

## Daily Start Workflow

Start the VM from the Arch Host:

```bash
virsh -c qemu:///system start ubuntu-server-lab
```

Check its state:

```bash
virsh -c qemu:///system domstate ubuntu-server-lab
```

Inspect the current DHCP lease if needed:

```bash
virsh -c qemu:///system net-dhcp-leases default
```

Inspect the Guest address associated with the VM:

```bash
virsh -c qemu:///system domifaddr \
  ubuntu-server-lab \
  --source lease
```

Connect:

```bash
ssh labuser@<VM_IP>
```

No login through `virt-viewer` is required before SSH.

---

## Daily Shutdown Workflow

### Shutdown from inside the SSH session

```bash
sudo poweroff
```

The SSH connection closes because the remote operating system stops.

Expected Host-side state:

```bash
virsh -c qemu:///system domstate ubuntu-server-lab
```

```text
shut off
```

### Execute shutdown directly through SSH

```bash
ssh -t labuser@<VM_IP> 'sudo poweroff'
```

### Request normal shutdown through libvirt

```bash
virsh -c qemu:///system shutdown ubuntu-server-lab
```

Both methods request an orderly operating-system shutdown.

Do not use the following command for routine shutdown:

```bash
virsh -c qemu:///system destroy ubuntu-server-lab
```

`destroy` is comparable to removing power from a physical machine and should
be reserved for an unresponsive VM.

---

## VM State Observation

One-time state check:

```bash
virsh -c qemu:///system domstate ubuntu-server-lab
```

Repeated state display without the `watch` title:

```bash
watch -t -n 1 \
  'virsh -c qemu:///system domstate ubuntu-server-lab'
```

`watch` is not a pager. It repeatedly redraws the terminal until interrupted
with `Ctrl+C`.

Log-style observation:

```bash
while true; do
  printf '%s  ' "$(date '+%H:%M:%S')"
  virsh -c qemu:///system domstate ubuntu-server-lab
  sleep 1
done
```

Wait only until the VM stops:

```bash
while [[ $(virsh -c qemu:///system domstate ubuntu-server-lab) != "shut off" ]]; do
  echo "$(date '+%H:%M:%S') VM is still running"
  sleep 1
done

echo "VM is shut off"
```

---

## Snapshot Operations

List snapshots:

```bash
virsh -c qemu:///system snapshot-list \
  ubuntu-server-lab \
  --tree
```

Show the current snapshot:

```bash
virsh -c qemu:///system snapshot-current \
  ubuntu-server-lab \
  --name
```

Create a snapshot before a risky exercise:

```bash
virsh -c qemu:///system snapshot-create-as \
  ubuntu-server-lab \
  before-risky-change \
  "Known-good state before controlled failure exercise" \
  --atomic \
  --validate
```

Prefer creating snapshots while the Guest is cleanly shut down unless the
exercise specifically requires a live snapshot.

Revert while the VM is shut down:

```bash
virsh -c qemu:///system snapshot-revert \
  ubuntu-server-lab \
  baseline-initial
```

Start after the rollback:

```bash
virsh -c qemu:///system start ubuntu-server-lab
```

Delete an obsolete snapshot only after verifying that it is no longer needed:

```bash
virsh -c qemu:///system snapshot-delete \
  ubuntu-server-lab \
  <SNAPSHOT_NAME>
```

---

## Routine Host Maintenance

### Update the Host

```bash
sudo pacman -Syu
```

After kernel, QEMU, libvirt, or systemd upgrades, plan a Host reboot.

### Validate services

```bash
systemctl is-active libvirtd virtlogd
systemctl --failed
```

### Validate libvirt resources

```bash
virsh -c qemu:///system list --all
virsh -c qemu:///system net-list --all
virsh -c qemu:///system pool-list --all
```

### Check storage capacity

```bash
df -h /var/lib/libvirt/images

sudo du -h \
  /var/lib/libvirt/images/ubuntu-server-lab.qcow2

sudo qemu-img info \
  /var/lib/libvirt/images/ubuntu-server-lab.qcow2
```

### Inspect snapshots

```bash
virsh -c qemu:///system snapshot-list \
  ubuntu-server-lab \
  --tree
```

Snapshots can increase storage use over time. Remove obsolete snapshots only
after confirming that their recovery points are no longer required.

---

## Routine Guest Maintenance

Start and connect:

```bash
virsh -c qemu:///system start ubuntu-server-lab
ssh labuser@<VM_IP>
```

Update packages:

```bash
sudo apt update
sudo apt full-upgrade
```

Check whether a reboot is needed:

```bash
test -f /var/run/reboot-required &&
  cat /var/run/reboot-required ||
  echo "reboot not required"
```

Check failed services:

```bash
systemctl --failed
```

Check filesystem usage:

```bash
df -h
lsblk -f
```

Check memory and load:

```bash
free -h
uptime
```

Check SSH state:

```bash
systemctl is-active ssh.socket ssh.service

sudo sshd -T |
  grep -E \
  '^(pubkeyauthentication|passwordauthentication|kbdinteractiveauthentication) '
```

Check logs from the current boot:

```bash
journalctl -b -p warning
```

Shut down cleanly when maintenance is complete:

```bash
sudo poweroff
```

---

## Troubleshooting: VM Does Not Start

Inspect state:

```bash
virsh -c qemu:///system domstate ubuntu-server-lab
virsh -c qemu:///system list --all
```

Inspect definition and disks:

```bash
virsh -c qemu:///system domblklist \
  ubuntu-server-lab \
  --details

virsh -c qemu:///system dumpxml \
  ubuntu-server-lab
```

Inspect libvirt logs:

```bash
sudo journalctl -b -u libvirtd
sudo journalctl -b -u virtlogd
```

Confirm the storage pool is active:

```bash
virsh -c qemu:///system pool-list --all
```

---

## Troubleshooting: No Bootable Device

Inspect attached block devices:

```bash
virsh -c qemu:///system domblklist \
  ubuntu-server-lab \
  --details
```

During installation, the CD-ROM should reference the ISO.

After installation, the disk should remain present and the ISO should normally
be ejected.

```text
disk:
vda → ubuntu-server-lab.qcow2

cdrom:
sda → ISO during installation
sda → empty after installation
```

---

## Troubleshooting: Guest Has No DHCP Address

Inspect the virtual network:

```bash
virsh -c qemu:///system net-list --all
ip -brief address show virbr0
virsh -c qemu:///system domiflist ubuntu-server-lab
bridge link show master virbr0
```

Inspect DHCP service:

```bash
sudo pgrep -a dnsmasq
sudo ss -lunp | grep -E ':(53|67)\b'
```

Capture traffic:

```bash
sudo tcpdump -ni virbr0 -e -vv \
  'udp port 67 or udp port 68'
```

Interpretation:

```text
No Discover:
Guest did not send a DHCP request.

Discover only:
Host firewall or dnsmasq response path is blocked.

Discover and Offer only:
Guest did not accept or process the response.

Discover, Offer, Request, and ACK:
DHCP succeeded; inspect Guest network application state.
```

Inspect leases:

```bash
virsh -c qemu:///system net-dhcp-leases default
```

---

## Troubleshooting: Guest Has IP but No Internet

Inspect Guest route:

```bash
ip route
```

Inspect Host forwarding:

```bash
sysctl net.ipv4.ip_forward
sudo iptables -vnL FORWARD --line-numbers
sudo iptables -t nat -vnL POSTROUTING --line-numbers
sudo nft -a list table ip libvirt_network
```

Inspect UFW:

```bash
sudo ufw status verbose
sudo iptables -vnL ufw-user-forward --line-numbers
```

Expected reasoning:

```text
Guest packet reaches virbr0
↓
libvirt forwarding allows it
↓
Host firewall must also permit forwarding
↓
libvirt NAT masquerades the packet
↓
external network receives it
```

---

## Troubleshooting: SSH Fails

Diagnose by layer:

```text
VM running?
↓
Guest has an IP address?
↓
Host can route to the Guest?
↓
TCP 22 is listening?
↓
Host firewall permits the path?
↓
SSH host key is correct?
↓
Public key is authorized?
↓
Authentication policy permits the selected method?
```

Host checks:

```bash
virsh -c qemu:///system domstate ubuntu-server-lab
virsh -c qemu:///system domifaddr \
  ubuntu-server-lab \
  --source lease
```

Guest console checks:

```bash
ip -brief address
ip route
systemctl status ssh.socket ssh.service
ss -lntp | grep ':22'
sudo sshd -t
sudo sshd -T
```

Verbose Host connection:

```bash
ssh -vvv labuser@<VM_IP>
```

---

## Troubleshooting: Host-Key Warning After Rollback

A snapshot rollback may restore an older SSH host key or Guest state.

Inspect the current Guest fingerprint from the console:

```bash
sudo ssh-keygen -lf /etc/ssh/ssh_host_ed25519_key.pub
```

Compare it with the Host record:

```bash
ssh-keygen -F <VM_IP>
```

Remove an obsolete entry only after verifying that the VM identity changed for
a legitimate reason:

```bash
ssh-keygen -R <VM_IP>
```

Reconnect and compare the new fingerprint before accepting it.

---

## Recovery Workflow

Use the following sequence after a failed experiment:

```text
Observe failure
↓
Record symptoms
↓
Attempt layer-based diagnosis
↓
Decide whether manual recovery is still educational
↓
Cleanly stop the VM when possible
↓
Revert to a known-good snapshot
↓
Start the VM
↓
Verify network, SSH, and services
```

Rollback:

```bash
virsh -c qemu:///system snapshot-revert \
  ubuntu-server-lab \
  baseline-initial
```

Start:

```bash
virsh -c qemu:///system start ubuntu-server-lab
```

Verify:

```bash
virsh -c qemu:///system domstate ubuntu-server-lab
virsh -c qemu:///system domifaddr \
  ubuntu-server-lab \
  --source lease

ssh \
  -o BatchMode=yes \
  -o PreferredAuthentications=publickey \
  -o PasswordAuthentication=no \
  labuser@<VM_IP>
```

Inside the Guest:

```bash
systemctl --failed
ip route
systemctl is-active ssh.socket ssh.service
```

---

## Important Host Paths

```text
VM images:
/var/lib/libvirt/images/

Primary VM disk:
/var/lib/libvirt/images/ubuntu-server-lab.qcow2

libvirt network dnsmasq configuration:
/var/lib/libvirt/dnsmasq/

UFW pre-input rules:
/etc/ufw/before.rules

libvirt service state:
/run/libvirt/
```

---

## Important Guest Paths

```text
OpenSSH main configuration:
/etc/ssh/sshd_config

OpenSSH drop-ins:
/etc/ssh/sshd_config.d/

Local SSH hardening:
/etc/ssh/sshd_config.d/00-local-hardening.conf

Authorized public keys:
~/.ssh/authorized_keys

Network declarations:
/etc/netplan/

Reboot requirement marker:
/var/run/reboot-required
```

---

## Safety Rules

- Use the VM rather than the Arch Host for destructive administration tests.
- Create a snapshot before risky configuration changes.
- Keep one working SSH session open while changing SSH settings.
- Validate `sshd` configuration with `sshd -t` before reloading it.
- Prefer `poweroff` or `virsh shutdown` over `virsh destroy`.
- Verify the target VM name before snapshot or destructive operations.
- Verify that `/dev/vda` belongs to the Guest before formatting it.
- Do not store passwords, private keys, MAC addresses, or real Host network
  identifiers in the public repository.
- Treat snapshots as recovery points, not independent backups.
- Check Host storage usage before accumulating multiple snapshots.

---

## Final Validation Checklist

### Host

- [x] CPU virtualization available
- [x] KVM device accessible
- [x] libvirt system connection works
- [x] libvirt services enabled
- [x] default network active and persistent
- [x] default storage pool active and persistent
- [x] UFW permits libvirt DHCP and DNS
- [x] UFW permits Guest-originated routed traffic
- [x] qcow2 disk stored in the libvirt image directory

### Guest

- [x] Ubuntu Server boots from the virtual disk
- [x] virtio network interface receives DHCP
- [x] default route points through the libvirt gateway
- [x] archive mirror is reachable
- [x] root filesystem uses LVM and ext4
- [x] OpenSSH is installed
- [x] SSH socket starts automatically
- [x] Host public key is authorized
- [x] public-key-only login succeeds
- [x] password SSH login is rejected
- [x] package updates applied
- [x] no failed systemd units
- [x] reboot persistence verified

### Recovery

- [x] installation ISO removed
- [x] clean shutdown verified
- [x] baseline snapshot created
- [x] baseline snapshot marked current
- [x] snapshot rollback command documented

---

## Operational Command Summary

Start:

```bash
virsh -c qemu:///system start ubuntu-server-lab
```

State:

```bash
virsh -c qemu:///system domstate ubuntu-server-lab
```

Find address:

```bash
virsh -c qemu:///system domifaddr \
  ubuntu-server-lab \
  --source lease
```

Connect:

```bash
ssh labuser@<VM_IP>
```

Shutdown from Guest:

```bash
sudo poweroff
```

Shutdown from Host:

```bash
virsh -c qemu:///system shutdown ubuntu-server-lab
```

Open console:

```bash
virt-viewer \
  --connect qemu:///system \
  --zoom=180 \
  --cursor=local \
  --hotkeys=release-cursor=ctrl+alt,toggle-fullscreen=shift+f11 \
  ubuntu-server-lab
```

List snapshots:

```bash
virsh -c qemu:///system snapshot-list \
  ubuntu-server-lab \
  --tree
```

Restore baseline:

```bash
virsh -c qemu:///system snapshot-revert \
  ubuntu-server-lab \
  baseline-initial
```

---

## Maintenance Principle

```text
Observe
↓
Predict
↓
Change
↓
Verify
↓
Preserve a known-good state
```

The VM is disposable as a laboratory system, but its operation should still be
deliberate, observable, and recoverable.
