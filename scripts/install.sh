#!/bin/bash
printf "\033[94m\033[1m"
cat <<EOF                          
         _                     _             _ _   
 ___ ___|_|___ ___ ___ ___ _ _| |_ _ _ ___ _| | |_ 
|   | . | |  _| -_| . |  _| | | . | | | . | . |  _|
|_|_|___|_|___|___|_  |_| |___|___|___|  _|___|_|  
                  |___|               |_|          
          NoiceGRUB Theme Installer v1.2

EOF

if [[ $(id -u) != "0" ]]
then
    printf "\033[91mCurrent user does not have root perms\n"
    exit
fi

printf "\033[92m[+] \033[94mCreating /boot/grub/themes/noicegrub\n"
mkdir -p /boot/grub/themes/noicegrub
printf "\033[92m[+] \033[94mCopying files\n"
cp ./export/* /boot/grub/themes/noicegrub
sed -i 's/.*GRUB_THEME=.*//' /etc/default/grub
echo "GRUB_THEME=/boot/grub/themes/noicegrub/theme.txt" >> /etc/default/grub
printf "\033[92m[+] \033[94mRunning update-grub\n\033[92m"
update-grub