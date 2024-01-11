#!/bin/bash

update_grub_func() {
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

get_path() {
    if [[ -d "/boot/grub2" ]]; then
    GRUB_PATH='/boot/grub2/'
    elif [[ -d "/boot/grub" ]]; then
    GRUB_PATH='/boot/grub/'
    elif [[ -d "/boot/efi/EFI/fedora" ]]; then
    GRUB_PATH='/boot/efi/EFI/fedora/'
    fi
}
