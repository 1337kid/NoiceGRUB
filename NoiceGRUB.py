from noicegrub import *
from noicegrub.template import NgCommonProps
from noicegrub.template.noice import NgNoiceTemplate
from noicegrub.template.theman import NgTheManTemplate
from noicegrub.template.mountains import NgMountainsTemplate
from noicegrub.template.nico import NgNicoTemplate
from rich import print as richprint
from rich.console import Console
from rich.markdown import Markdown
from rich.prompt import IntPrompt,Confirm
from rich.panel import Panel
import os

init()
console = Console()

richprint(Panel("[cyan bold]" + banner + "[/cyan bold]",width=65,border_style="cyan"))
table,preset_dict = preset_table()
console.print(table)
richprint("[cyan bold][ 0 ][/cyan bold] [green bold]Instructions for creating a preset[/green bold]")
richprint("[cyan bold][ 99 ][/cyan bold] [green bold]Remove installed NoiceGRUB theme[/green bold]")

choice = IntPrompt.ask("[yellow]Choice[/yellow]",choices=gen_choices(preset_dict))
if choice == 0:
    console.print(Markdown(open('noicegrub/createpreset.md').read()))
    exit()
elif choice == 99:
    richprint('\n[green bold]Executing scripts/remove.sh ... [/green bold]')
    os.system('sudo ./scripts/remove.sh')
    richprint('[green bold]Done[/green bold]')
    exit()    

print()
preset = get_preset(preset_dict[choice])
table = preset_info_table(preset)
console.print(table)
font_file = preset[1]['font_family']
if not os.path.exists(f'./fonts/{font_file}'):
    richprint(f'[red bold][Error] {font_file} is not present in ./fonts/ [/red bold]')
    exit()
choice = Confirm.ask("[yellow bold]Would you like to customise the font ?[/yellow bold]")
if choice:
    table,fonts = font_table()
    console.print(table)
    font_choice = IntPrompt.ask("[yellow]Choice[/yellow]",choices=[str(i) for i in range(1,len(fonts)+1)])
    preset[1]['font_family'] = fonts[font_choice]
    font_size = IntPrompt.ask("[yellow]Font size in pixels (integer) [/yellow]")
    preset[1]['selection_font'] = font_size

if preset[0]=='Kewl': NgCommonProps(preset).export_theme()
elif preset[0]=='Noice': NgNoiceTemplate(preset).export_theme()
elif preset[0]=='TheMan': NgTheManTemplate(preset).export_theme()
elif preset[0]=='Mountains': NgMountainsTemplate(preset).export_theme()
elif preset[0]=='Nico': NgNicoTemplate(preset).export_theme()

richprint('\n[cyan bold]Generated theme has been placed in ./export/ [/cyan bold]')
choice = Confirm.ask("[yellow bold]Would you like to install the theme ?[/yellow bold]")
if choice:
    richprint('\n[green bold]Executing scripts/install.sh ... [/green bold]')
    os.system('sudo ./scripts/install.sh')
richprint('[green bold]Done[/green bold]')