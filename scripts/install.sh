#!/bin/bash

GRUB_PATH=''
THEME_PATH=''

source ./scripts/functions.sh

makefont() {
    font=$(ls ./export | grep -E '.ttf|.otf')
    size=$(echo $font | awk -F '.' '{print $2}')
    name="$(echo $font | awk -F '.' '{print $1}').pf2"
    if [[ $(which grub2-mkfont) != "" ]];then
        grub2-mkfont -s $size -o $THEME_PATH/$name ./export/$font 2>/dev/null
    else
        grub-mkfont -s $size -o $THEME_PATH/$name ./export/$font 2>/dev/null
    fi
    echo $name
}

install() {
    printf "\033[92m[+] \033[94mCreating $THEME_PATH\n"
    rm -r $THEME_PATH 2> /dev/null
    mkdir -p $THEME_PATH
    printf "\033[92m[+] \033[94mCopying files\n"
    cp ./export/* $THEME_PATH

    #======== /etc/default/grub config file 
    sed -i 's/.*GRUB_THEME=.*//' /etc/default/grub
    echo "GRUB_THEME=$THEME_PATH/theme.txt" >> /etc/default/grub #theme location
    font_name=$(makefont)
    sed -i 's/.*GRUB_FONT=.*//' /etc/default/grub
    echo "GRUB_FONT=$THEME_PATH/$font_name" >> /etc/default/grub #font location

    #========= GRUB update
    #
    printf "\033[92m[+] \033[94mUpdating GRUB config\n\033[92m"
    update_grub_func
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
echo "Generated theme will be placed in $THEME_PATH"
install