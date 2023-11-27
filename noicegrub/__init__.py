import os,toml
from rich.table import Table

def get_preset(name):
	data=toml.load(open(f'./presets/{name}.toml'))
	return [data[i] for i in data]

def preset_table():
    preset_dict={}
    files=os.listdir('presets')
    files.sort()
    table = Table(title="Available Presets")
    table.add_column("No", justify="right", style="cyan", no_wrap=True)
    table.add_column("Preset", justify="left", style="green", no_wrap=True)
    table.add_column("Template", justify="left", style="green", no_wrap=True)
    presets=[{i.split('.')[0]:toml.load(open(f'presets/{i}'))['template']} for i in files]
    for i in presets:
        preset=list(i.keys())[0]
        table.add_row(str(presets.index(i)+1),preset,i[preset])
        preset_dict[presets.index(i)+1]=preset
    return table,preset_dict

banner = '''                                                
o    o         o               .oPYo.  .oPYo. o    o  .oPYo. 
8b   8                         8    8  8   `8 8    8  8   `8 
8`b  8 .oPYo. o8 .oPYo. .oPYo. 8      o8YooP' 8    8 o8YooP' 
8 `b 8 8    8  8 8    ' 8oooo8 8   oo  8   `b 8    8  8   `b 
8  `b8 8    8  8 8    . 8.     8    8  8    8 8    8  8    8 
8   `8 `YooP'  8 `YooP' `Yooo' `YooP8  8    8 `YooP'  8oooP' 
..:::..:.....::..:.....::.....::....8 :..:::..:.....::......:
:::::::: @1337kid ::::::::::::::::::8 ::::::: v1.8.3 ::::::::\n'''