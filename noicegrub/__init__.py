import os,toml
from rich.table import Table

def get_preset(name):
	data=toml.load(open(f'./presets/{name}.toml'))
	return [data[i] for i in data]


#================= rich tables
def preset_table():
    preset_dict={}
    files=os.listdir('presets')
    files.sort()
    table = Table(title="Available Presets")
    table.add_column("No.", justify="right", style="cyan", no_wrap=True)
    table.add_column("Preset", justify="left", style="green", no_wrap=True)
    table.add_column("Template", justify="left", style="green", no_wrap=True)
    presets=[{i.split('.')[0]:toml.load(open(f'presets/{i}'))['template']} for i in files]
    for i in presets:
        preset=list(i.keys())[0]
        table.add_row(str(presets.index(i)+1),preset,i[preset])
        preset_dict[presets.index(i)+1]=preset
    return table,preset_dict

def preset_info_table(preset_conf):
    table = Table(title="Selected Preset Info")
    table.add_column("Template",justify="left", style="cyan", no_wrap=True)
    table.add_column("Font Family",justify="left", style="green", no_wrap=True)
    table.add_column("Size (pixels)",justify="left", style="green", no_wrap=True)
    table.add_row(preset_conf[0],preset_conf[1]['font_family'],preset_conf[1]['selection_font'])
    return table

def font_table():
    print()
    fonts={}
    files=os.listdir('fonts')
    table = Table(title="Available Fonts")
    table.add_column("No.",justify="right", style="cyan", no_wrap=True)
    table.add_column("Font Family",justify="left", style="green", no_wrap=True)
    for i in range(len(files)):
        fonts[i+1]=files[i]
        table.add_row(str(i+1),files[i])
    return table,fonts

#=================

def gen_font_name(font_name,size):
    font_name=font_name.split('.')
    return f"export/{font_name[0]}.{size}.{font_name[1]}"

banner = '''                                                
o    o         o               .oPYo.  .oPYo. o    o  .oPYo. 
8b   8                         8    8  8   `8 8    8  8   `8 
8`b  8 .oPYo. o8 .oPYo. .oPYo. 8      o8YooP' 8    8 o8YooP' 
8 `b 8 8    8  8 8    ' 8oooo8 8   oo  8   `b 8    8  8   `b 
8  `b8 8    8  8 8    . 8.     8    8  8    8 8    8  8    8 
8   `8 `YooP'  8 `YooP' `Yooo' `YooP8  8    8 `YooP'  8oooP' 
..:::..:.....::..:.....::.....::....8 :..:::..:.....::......:
:::::::: @1337kid ::::::::::::::::::8 :::::::: v2.0 :::::::::\n'''