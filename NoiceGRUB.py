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

console = Console()

richprint(Panel("[cyan bold]" + banner + "[/cyan bold]",width=65,border_style="cyan"))
table,preset_dict = preset_table()
console.print(table)
richprint("[cyan bold][ 0 ][/cyan bold] [green bold]Instructions for creating a preset[/green bold]")

choice = IntPrompt.ask("[yellow]Choice[/yellow]",choices=[str(i) for i in range(len(os.listdir('presets'))+1)])
if choice==0:
    console.print(Markdown(open('noicegrub/createpreset.md').read()))
    exit()
preset = get_preset(preset_dict[choice])

if preset[0]=='Kewl': NgCommonProps(preset).export_theme()
elif preset[0]=='Noice': NgNoiceTemplate(preset).export_theme()
elif preset[0]=='TheMan': NgTheManTemplate(preset).export_theme()
elif preset[0]=='Mountains': NgMountainsTemplate(preset).export_theme()
elif preset[0]=='Nico': NgNicoTemplate(preset).export_theme()

richprint('\n[green bold]Executing scripts/install.sh ... [/green bold]')
os.system('chmod +x ./scripts/install.sh')
os.system('sudo ./scripts/install.sh')
richprint('[green bold]Thankyou for using NoiceGRUB[/green bold]')