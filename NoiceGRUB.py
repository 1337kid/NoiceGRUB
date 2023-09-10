from core.main import generate_theme,banner,menu
from colorama import Fore, Style
import re,os

print(Fore.CYAN + banner() + Style.RESET_ALL)
print(Fore.GREEN + menu() + Style.RESET_ALL)
choice=input(Fore.YELLOW+'Choice: '+Style.RESET_ALL)
if choice not in '0123456':
    print(Fore.RED + 'Invalid choice')
    exit()
if choice=='0':
    input_msgs=['Primary gradient colour in hex: ','Secondary gradient colour in hex: ','GRUB selection background colour in hex: ','GRUB selection font colour: ','GRUB font colour in hex: ','GRUB countdown colour in hex: ']
    data=[]
    for i in range(6):
        colour=input(Fore.YELLOW + input_msgs[i] + Fore.WHITE)
        if not '#' in colour:colour='#'+colour
        match = re.search(r'^#(?:[0-9a-fA-F]{3}){1,2}$', colour)
        if not match:
            print(Fore.RED + 'Invalid colour code')
            exit()
        data.append(colour)
    generate_theme(False,[{'primary':data[0],'secondary':data[1],'selection_bg_colour':data[2]},{'font_colour':data[4],'selection_font_colour':data[3],'label_colour':data[5]}])
else:
    options={'1':'chocolate','2':'lightlime','3':'noice','4':'thesky','5':'vioblue','6':'wildfire'}
    generate_theme(options[choice])
install_theme=input(Fore.YELLOW + 'Do you want to place the generated theme in /boot/grub/themes/ (Y/N)? ' + Fore.WHITE).lower()
if install_theme=='y':
    print('\n'+Fore.CYAN)
    os.system('chmod +x ./scripts/install.sh')
    os.system('sudo ./scripts/install.sh')
print('\n' + Fore.GREEN + 'Thankyou for using NoiceGRUB' + Style.RESET_ALL)