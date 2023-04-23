import xmltodict,cairosvg,os,toml
from colorama import Fore, Style
import re

def banner():
	return '''                                                
o    o         o               .oPYo.  .oPYo. o    o  .oPYo. 
8b   8                         8    8  8   `8 8    8  8   `8 
8`b  8 .oPYo. o8 .oPYo. .oPYo. 8      o8YooP' 8    8 o8YooP' 
8 `b 8 8    8  8 8    ' 8oooo8 8   oo  8   `b 8    8  8   `b 
8  `b8 8    8  8 8    . 8.     8    8  8    8 8    8  8    8 
8   `8 `YooP'  8 `YooP' `Yooo' `YooP8  8    8 `YooP'  8oooP' 
..:::..:.....::..:.....::.....::....8 :..:::..:.....::......:
:::::::: @1337kid ::::::::::::::::::8 ::::::: v1.2 ::::::::::'''

def menu():
	return '''
Available presets
~~~~~~~~~~~~~~~~~
>> Kewl Template
[1] Chocolate	 [4] VioBlue
[2] Lightlime    [5] Wildfire
[3] TheSky

>> Noice Template
[6] Noice
~~~~~~~~~~~~~~~~~~~~~~~~~~~~
[0] Custom
'''

def template_menu():
	return '''
Availabe Templates
[1] Kewl
[2] Noice

Choice:
'''

def check_colour_code(colour):
    if not '#' in colour:colour='#'+colour
    match = re.search(r'^#(?:[0-9a-fA-F]{3}){1,2}$', colour)
    if not match:
        print(Fore.RED + 'Invalid colour code')
        exit()
    return colour

def get_preset(name):
	data=toml.load(open(f'./presets/{name}.toml'))
	return [data[i] for i in data]

#=============================================================
def generate_background(template,primary,secondary,extra=None):
	svg_temp=xmltodict.parse(open(f'template/{template}.svg').read())
	if template=='kewl':   # For Kewl Template
		svg_temp['svg']['defs']['linearGradient']['stop'][0]['@stop-color']=primary
		svg_temp['svg']['defs']['linearGradient']['stop'][1]['@stop-color']=secondary
	elif template=='noice':# For Noice Template
		'''
		'extra' argument format
		~~~~~~~~~~~~~~~~~~~~~
		'''
		# Background Gradient
		svg_temp['svg']['defs']['linearGradient'][0]['stop'][0]['@stop-color']=primary
		svg_temp['svg']['defs']['linearGradient'][0]['stop'][1]['@stop-color']=secondary
		svg_temp['svg']['rect'][1]['@fill']=extra['menuboxbg'][0]
		# Topright Polygon gradient
		svg_temp['svg']['defs']['linearGradient'][1]['stop'][0]['@stop-color']=extra['polygon'][0]
		svg_temp['svg']['defs']['linearGradient'][1]['stop'][1]['@stop-color']=extra['polygon'][1]
		# Bottomright ellipse gradient
		svg_temp['svg']['defs']['linearGradient'][2]['stop'][0]['@stop-color']=extra['ellipse'][0]
		svg_temp['svg']['defs']['linearGradient'][2]['stop'][1]['@stop-color']=extra['ellipse'][1]
		# Topleft quarter circle gradient
		svg_temp['svg']['defs']['linearGradient'][3]['stop'][0]['@stop-color']=extra['circle'][0]
		svg_temp['svg']['defs']['linearGradient'][3]['stop'][1]['@stop-color']=extra['circle'][1]
		# Bottomleft triangle colour
		svg_temp['svg']['path'][0]['@fill']=extra['triangle'][0]
	open('temp1.svg','w').write(xmltodict.unparse(svg_temp,pretty=True))
	if template=='noice':
		data=open('temp1.svg').readlines()
		menu_box=data.pop(3)
		data.insert(9,menu_box)
		open('temp1.svg','w').writelines(data)
	cairosvg.svg2png(url='temp1.svg', write_to=f'./export/background.png')
	#os.remove('temp.svg')

def export_selection_png(primary):
	filenames=['select_c','select_e','select_w']
	for i in filenames:
		svg_temp=xmltodict.parse(open(f'template/{i}.svg').read())
		if primary:
			svg_temp['svg']['path']['@fill']=primary
		open('temp.svg','w').write(xmltodict.unparse(svg_temp))
		cairosvg.svg2png(url='temp.svg', write_to=f'./export/{i}.png')
		os.remove('temp.svg')

def export_theme_config(font_colour,selection_font_colour,label_colour):
	config=open('template/theme.txt').read()
	config=config.replace('{font_colour}',f'"{font_colour}"')
	config=config.replace('{selection_font_colour}',f'"{selection_font_colour}"')
	config=config.replace('{label_colour}',f'"{label_colour}"')
	open('./export/theme.txt','w').write(config)
#=============================================================

def generate_theme(name=True,custom=False):
	if not os.path.exists('export'):os.makedirs('export')
	print(Fore.GREEN + '~ Generating theme' + Style.RESET_ALL)
	if name:
		data=get_preset(name)
	if custom:
		data=custom
	if data[0]=='kewl':
		generate_background('kewl',data[1]['primary'],data[1]['secondary'])
	elif data[0]=='noice':
		generate_background('noice',data[1]['primary'],data[1]['secondary'],data[3])
	export_selection_png(data[1]['selection_bg_colour'])
	export_theme_config(data[2]['font_colour'],data[2]['selection_font_colour'],data[2]['label_colour'])
	print(Fore.GREEN + f"~ Generated theme saved to {os.getcwd()+'/export/'}" + Style.RESET_ALL)