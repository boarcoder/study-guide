## Linux boot process

https://www.youtube.com/watch?v=XpFsMB6FoOs

1. Power on
2. BIOS/UEFI

BIOS is master boot record (2TB)
Slower boot
Less secure

UEFI is GUID partition table (GPT)
with no size constraints
Faster boot
Secure boot

3. POST - Power on self test
Checks all hardware is working
If not, POST error.

4. BIOS load the boot load software in order (usb, hard drive)

5. MBR bootloader or .efi bootloader.
- Locate operating system
- Load kernel into memory
- Run kernel code

6. GRUB2 or LILO
GRUB2 very full featured today.

7. Kernel load into memory.

8. Kernel take over resources
- Device drivers
Kernel module
Background processes

9. Systemd init
-systemctl
-journalctl
-notify
-analyze
-cfgls
-cgtop
-loginctl
-nspawn

Daemons
Targets
Kernel
Core
Libraries

10. systemd default.target tells what mode to boot into.
