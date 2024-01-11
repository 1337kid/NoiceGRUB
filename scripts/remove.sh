#!/bin/bash

GRUB_PATH=''

if [[ $(id -u) != "0" ]]
then
    printf "\033[91mCurrent user does not have root perms\n"
    exit
fi

source ./scripts/functions.sh

printf "\033[1m"
get_path
THEME_PATH=$GRUB_PATH"themes/noicegrub"
printf "\033[92m[+] \033[94mRemoving NoiceGRUB theme\n\033[92m"
rm -rf $THEME_PATH 2>/dev/null
#===== grub config
sed -i 's/.*GRUB_THEME=.*//' /etc/default/grub
sed -i 's/.*GRUB_FONT=.*//' /etc/default/grub
#=====
printf "\033[92m[+] \033[94mUpdating GRUB config\n\033[92m"
update_grub_func