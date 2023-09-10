#!/bin/bash
if [[ $(id -u) != "0" ]]
then
    echo "Current user does not have root perms"
    exit
fi

mkdir -p /boot/grub/themes
cp -r ./noicegrub /boot/grub/themes
echo "GRUB_THEME=/boot/grub/themes/noicegrub/theme.txt" >> /etc/default/grub
update-grub
echo "NoiceGRUB theme has been placed in '/boot/grub/themes'. You may now reboot your PC"
