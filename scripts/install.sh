#!/bin/bash

THEMES_PATH=''

#==========================
get_path() {
    if [[ -d "/boot/grub2" ]]; then
    THEMES_PATH='/boot/grub2/themes/noicegrub'
    elif [[ -d "/boot/grub" ]]; then
    THEMES_PATH='/boot/grub/themes/noicegrub'
    elif [[ -d "/boot/efi/EFI/fedora" ]]; then
    THEMES_PATH='/boot/efi/EFI/fedora/themes/noicegrub'
    fi
}

get_path
#=========================

printf "\033[94m\033[1m"
cat <<EOF                          
         _                     _             _ _   
 ___ ___|_|___ ___ ___ ___ _ _| |_ _ _ ___ _| | |_ 
|   | . | |  _| -_| . |  _| | | . | | | . | . |  _|
|_|_|___|_|___|___|_  |_| |___|___|___|  _|___|_|  
                  |___|               |_|          
          NoiceGRUB Theme Installer

EOF

if [[ $(id -u) != "0" ]]
then
    printf "\033[91mCurrent user does not have root perms\n"
    exit
fi

printf "\033[92m[+] \033[94mCreating $THEMES_PATH\n"
mkdir -p $THEMES_PATH
printf "\033[92m[+] \033[94mCopying files\n"
cp ./export/* $THEMES_PATH
sed -i 's/.*GRUB_THEME=.*//' /etc/default/grub
echo "GRUB_THEME=$THEMES_PATH/theme.txt" >> /etc/default/grub
#
#========= GRUB update
#
printf "\033[92m[+] \033[94mUpdating GRUB config\n\033[92m"
if [[ $(which dnf) != "" ]];then
    grub2-mkconfig -o /boot/grub2/grub2.cfg
else
    update-grub