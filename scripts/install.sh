#!/bin/bash
if [[ $(id -u) != "0" ]]
then
    echo "Current user does not have root perms"
    exit
fi

mkdir -p /boot/grub/themes/noicegrub
cp ./export/* /boot/grub/themes/noicegrub
sed -i 's/.*GRUB_THEME=.*//' /etc/default/grub
echo "GRUB_THEME=/boot/grub/themes/noicegrub/theme.txt" >> /etc/default/grub
update-grub