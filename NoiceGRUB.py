from noicegrub import *
from noicegrub.template import NgCommonProps
from noicegrub.template.noice import NgNoiceTemplate
from noicegrub.template.theman import NgTheManTemplate
from noicegrub.template.mountains import NgMountainsTemplate
from colorama import Style,Fore

print(Fore.CYAN + banner + Style.RESET_ALL)
table,preset_dict = preset_table()
print(Fore.GREEN +'\nAvailable Presets\n', table ,'\n\nInstructions for creating a preset can be found in README.md\n'+Style.RESET_ALL,sep='')

try:
    choice=int(input(Fore.YELLOW+'Choice: '+Style.RESET_ALL))
    if choice not in range(1,9):
        print(Fore.RED + 'Invalid choice' + Style.RESET_ALL)
        exit()
except ValueError:
    print(Fore.RED + 'Not an integer' + Style.RESET_ALL)
    exit()

preset = get_preset(preset_dict[choice])

if preset[0]=='Kewl': NgCommonProps(preset).export_theme()
elif preset[0]=='Noice': NgNoiceTemplate(preset).export_theme()
elif preset[0]=='TheMan': NgTheManTemplate(preset).export_theme()
elif preset[0]=='Mountains': NgMountainsTemplate(preset).export_theme()

install_theme=input(Fore.YELLOW + 'Do you want to place the generated theme in /boot/grub/themes/ (Y/N)? ' + Fore.WHITE).lower()
if install_theme=='y':
    print('\n'+Fore.CYAN)
    os.system('chmod +x ./scripts/install.sh')
    os.system('sudo ./scripts/install.sh')
print('\n' + Fore.GREEN + 'Thankyou for using NoiceGRUB' + Style.RESET_ALL)