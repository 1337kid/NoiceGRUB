from core.main import generate_theme,banner,menu,check_colour_code,template_menu
from colorama import Fore, Style
import os
from core.msgs import *

print(Fore.CYAN + banner() + Style.RESET_ALL)
print(Fore.GREEN + menu() + Style.RESET_ALL)
choice=input(Fore.YELLOW+'Choice: '+Style.RESET_ALL)
if choice not in '0123456':
    print(Fore.RED + 'Invalid choice')
    exit()
if choice=='0':
    template=input(Fore.YELLOW + template_menu() + Style.RESET_ALL)
    if template not in '12':
        print(Fore.RED + 'Invalid choice')
        exit()
    #=================
    data=[]
    for i in range(7):
        colour=input(Fore.YELLOW + input_msgs[i] + Fore.WHITE)
        colour=check_colour_code(colour)
        data.append(colour)
    # ***
    background_conf={'primary':data[0],'secondary':data[1],'selection_bg_colour':data[2]}
    theme_text_conf={'font_colour':data[4],'selection_font_colour':data[3],'label_colour':data[5]}
    # ***
    if template=='1':
        generate_theme(False,['kewl',background_conf,theme_text_conf])
    elif template=='2':  # Getting extra colour values for noice template
        extra={}
        for i in noice_theme_extra:
            temp=[]
            for j in noice_theme_extra[i]:
                colour=input(Fore.YELLOW + j + Fore.WHITE)
                colour=check_colour_code(colour)
                temp.append(colour)
            extra[i]=temp
        generate_theme(False,['noice',background_conf,theme_text_conf,extra])
else:
    options={'1':'chocolate','2':'lightlime','3':'thesky','4':'vioblue','5':'wildfire','6':'noice'}
    generate_theme(options[choice])
install_theme=input(Fore.YELLOW + 'Do you want to place the generated theme in /boot/grub/themes/ (Y/N)? ' + Fore.WHITE).lower()
if install_theme=='y':
    print('\n'+Fore.CYAN)
    os.system('chmod +x ./scripts/install.sh')
    os.system('sudo ./scripts/install.sh')
print('\n' + Fore.GREEN + 'Thankyou for using NoiceGRUB' + Style.RESET_ALL)