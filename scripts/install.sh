#!/bin/bash

GRUB_PATH=''
THEMES_PATH=''

get_path() {
    if [[ -d "/boot/grub2" ]]; then
    GRUB_PATH='/boot/grub2/'
    elif [[ -d "/boot/grub" ]]; then
    GRUB_PATH='/boot/grub/'
    elif [[ -d "/boot/efi/EFI/fedora" ]]; then
    GRUB_PATH='/boot/efi/EFI/fedora/'
    fi
}


install() {
    printf "\033[92m[+] \033[94mCreating $THEME_PATH\n"
    mkdir -p $THEME_PATH
    printf "\033[92m[+] \033[94mCopying files\n"
    cp ./export/* $THEME_PATH
    sed -i 's/.*GRUB_THEME=.*//' /etc/default/grub
    echo "GRUB_THEME=$THEME_PATH/theme.txt" >> /etc/default/grub
    #
    #========= GRUB update
    #
    printf "\033[92m[+] \033[94mUpdating GRUB config\n\033[92m"
    if [[ $(which dnf) != "" ]];then
        fedora_version=$(cat /etc/fedora-release | awk '{print $3}')
        if [[ fedora_version -gt 34 ]];then
            grub2-mkconfig -o /boot/grub2/grub.cfg
        else
            grub2-mkconfig -o /boot/efi/EFI/fedora/grub.cfg
        fi
    else
        update-grub
    fi
}
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

get_path
THEME_PATH=$GRUB_PATH"themes/noicegrub"
printf "\033[1m\033[93m"
read -p "Do you want to place the generated theme in $GRUB_PATH [y/n] " inst
case $inst in
    [Yy]* ) install;;
    * ) exit;;
esac