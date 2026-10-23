*This activity has been created as part of the 42 curriculum by aal-moum.*

# Born2beroot

## Description

Born2beroot is the first system administration project in the 42 curriculum.

The goal of this activity is to introduce the fundamentals of virtualization, Linux system administration, and server security.

The project consists of setting up a secure virtual machine while following strict rules for:

* System installation and configuration
* User and group management
* Privilege management
* SSH configuration
* Firewall configuration
* Password policies
* Disk partitioning and encryption
* System monitoring and automation

The final system is configured as a minimal server without a graphical interface.

---

## Instructions

The virtual machine can be created using **VirtualBox** or **UTM**.

After starting the machine, log in using the configured non-root user.

### SSH

The SSH service is configured to listen on port `4242`.

```bash
ssh <username>@<ip_address> -p 4242
```

Root login through SSH is disabled for security reasons.

### Firewall

The firewall is configured to allow incoming connections only through port `4242`.

### Monitoring

A Bash script named `monitoring.sh` is used to monitor the system.

The script is executed at startup and every 10 minutes using `cron`. Its output is broadcast to all active terminals.

---

# Project Description

## Operating System Choice

### Debian

Debian was chosen as the operating system for this project.

#### Advantages

* Highly stable and reliable
* Lightweight
* Large software repository
* Strong community support
* Powerful `apt` package manager
* Strong focus on free and open-source software

#### Disadvantages

* Stable releases prioritize reliability over the newest software versions
* Packages can be older compared to more cutting-edge distributions

### Rocky Linux

Rocky Linux is an enterprise-oriented Linux distribution designed to be compatible with Red Hat Enterprise Linux (RHEL).

It is commonly used in enterprise and server environments where stability, predictable releases, and long-term support are important.

### Debian vs Rocky Linux

| Debian                                       | Rocky Linux                                  |
| -------------------------------------------- | -------------------------------------------- |
| Community-driven                             | Enterprise-oriented                          |
| Focuses on stability and universal usability | Focuses on enterprise compatibility          |
| Uses `apt`/`dpkg`                            | Uses `dnf`/RPM                               |
| Common on general-purpose servers            | Common in RHEL-based enterprise environments |
| Lightweight and flexible                     | Enterprise-focused and highly structured     |

Debian was selected because it provides a stable and lightweight environment while keeping system administration relatively straightforward.

---

## Main Design Choices

### Partitioning and LVM

The system uses **LVM (Logical Volume Management)** with encrypted partitions.

Encryption protects data at rest, while LVM provides flexible management of logical volumes.

This allows storage to be managed and resized more easily without having to recreate the entire disk layout.

The general structure is:

```text
Physical Disk
      │
      ▼
Encrypted Partition
      │
      ▼
Physical Volume (PV)
      │
      ▼
Volume Group (VG)
      │
      ├── Logical Volume
      ├── Logical Volume
      └── Logical Volume
```

---

### Security Policies

A strong password policy is enforced using **PAM** and `libpam-pwquality`.

The policy includes requirements such as:

* Minimum password length
* Uppercase letters
* Lowercase letters
* Numbers
* Password expiration
* Minimum time between password changes
* Password history restrictions

SSH root login is disabled to prevent direct remote access to the root account.

---

### User Management

A dedicated non-root user is created for normal administration.

The user belongs to the required:

* `user42`
* `sudo`

groups.

Administrative operations requiring elevated privileges are performed using `sudo` instead of logging in directly as root.

---

### Sudo

`sudo` is configured according to the project's security requirements.

The configuration includes:

* Limited authentication attempts
* A custom error message for incorrect passwords
* Logging of sudo activity
* TTY mode enabled
* Restricted executable paths

Sudo logs are stored in:

```text
/var/log/sudo/
```

---

### SSH

The SSH service is configured to listen exclusively on port:

```text
4242
```

Root login through SSH is disabled.

This provides a controlled method for remotely accessing and administering the server.

---

### Firewall

The system uses **UFW (Uncomplicated Firewall)**.

Only port `4242` is allowed for incoming connections, while other unnecessary incoming connections are blocked.

---

# Monitoring Script

The project includes a Bash script named `monitoring.sh`.

It displays system information at startup and every 10 minutes.

The script monitors:

* Operating system architecture
* Kernel version
* Number of physical processors
* Number of virtual processors
* RAM usage and utilization percentage
* Storage usage and utilization percentage
* CPU utilization
* Date and time of the last reboot
* LVM status
* Number of active TCP connections
* Number of logged-in users
* IPv4 address
* MAC address
* Number of commands executed using `sudo`

The script is scheduled using `cron` and its output is broadcast to the active terminals.

---

# Required Comparisons

## AppArmor vs SELinux

Both **AppArmor** and **SELinux** provide Mandatory Access Control (MAC).

### AppArmor

AppArmor uses security profiles that primarily define access based on filesystem paths.

**Advantages:**

* Easier to understand
* Easier to configure
* Path-based policies are relatively intuitive
* Commonly used with Debian-based systems

### SELinux

SELinux uses security contexts and labels associated with files, processes, and other system resources.

**Advantages:**

* Highly granular access control
* Powerful security policy system
* Widely used in RHEL-based systems

### Comparison

| AppArmor                | SELinux                 |
| ----------------------- | ----------------------- |
| Mainly path-based       | Context and label-based |
| Easier to configure     | More complex            |
| Easier for beginners    | More advanced           |
| Common on Debian/Ubuntu | Common on Rocky/RHEL    |

---

## UFW vs firewalld

### UFW

**UFW (Uncomplicated Firewall)** provides a simple command-line interface for configuring firewall rules.

Example:

```bash
sudo ufw allow 4242/tcp
sudo ufw status
```

It is well suited for straightforward firewall configurations.

### firewalld

`firewalld` is commonly used on RHEL-based systems such as Rocky Linux.

It provides concepts such as:

* Zones
* Services
* Ports
* Rich rules
* Runtime configuration
* Permanent configuration

It is designed to manage firewall rules dynamically.

### Comparison

| UFW                     | firewalld                         |
| ----------------------- | --------------------------------- |
| Simple interface        | More advanced configuration       |
| Easy to learn           | More complex                      |
| Rule-based management   | Zone and service-based management |
| Common on Debian/Ubuntu | Common on Rocky/RHEL              |

---

## VirtualBox vs UTM

### VirtualBox

VirtualBox is a cross-platform virtualization platform that can run virtual machines on Windows, Linux, and macOS.

It is widely used for virtualization and is particularly common in x86/x86-64 environments.

### UTM

UTM is a virtualization and emulation application designed primarily for macOS.

It can use Apple's Hypervisor framework for supported virtualization workloads and is particularly useful on Apple Silicon Macs.

### Comparison

| VirtualBox                          | UTM                                  |
| ----------------------------------- | ------------------------------------ |
| Windows, Linux, macOS               | Primarily macOS                      |
| General-purpose virtualization      | Virtualization and emulation         |
| Widely used on x86/x86-64           | Particularly useful on Apple Silicon |
| Traditional VM management interface | macOS-oriented interface             |

---

# Resources

The following resources were used to understand and configure the system:

* [Debian Documentation](https://www.debian.org/doc/)
* [ArchWiki](https://wiki.archlinux.org/)
* Linux `man` pages
* 42 Born2beroot subject

### AI Usage

Artificial intelligence was used as a supporting tool during the creation of this README.

It was used to:

* Structure and organize the README
* Improve the formatting and readability of technical comparisons
* Clarify the logic behind the Bash monitoring script
* Help explain system administration concepts

The system configuration and implementation were performed as part of the project work.

