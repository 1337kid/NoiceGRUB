#!/bin/bash

GRUB_PATH=''

source ./scripts/functions.sh

printf "\033[1m"
check_uid
get_path
THEME_PATH=$GRUB_PATH"themes/noicegrub"
printf "\033[92m[+] \033[94mRemoving NoiceGRUB theme\n\033[92m"
rm -rf $THEME_PATH 2>/dev/null
#===== grub config
printf "\033[92m[+] \033[94mRestoring GRUB config\n\033[92m"
printf "\033[92m[+] \033[94mChecking for backup (/etc/default/grub.bak)\n\033[92m"
if [[ -f /etc/default/grub.bak ]]; then
    rm /etc/default/grub
    mv /etc/default/grub.bak /etc/default/grub
else
    printf "\033[92m[+] \033[94mChecking for default config (/usr/share/grub/default/grub)\n\033[92m"
    if [[ -f /usr/share/grub/default ]]; then
        rm /etc/default/grub
        mv /usr/share/grub/default/grub /etc/default/grub
    else
        printf "\033[91mError: Could not find backup config\n"
        printf "\033[92m[+] \033[94mModifyng present config\n\033[92m"
        sed -i 's/.*GRUB_THEME=.*//' /etc/default/grub
        sed -i 's/.*GRUB_FONT=.*//' /etc/default/grub
    fi
fi
#=====
printf "\033[92m[+] \033[94mUpdating GRUB config\n\033[92m"
update_grub_func