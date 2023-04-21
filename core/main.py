import xmltodict,cairosvg,os,toml
from colorama import Fore, Style

def banner():
	return '''                                                
o    o         o               .oPYo.  .oPYo. o    o  .oPYo. 
8b   8                         8    8  8   `8 8    8  8   `8 
8`b  8 .oPYo. o8 .oPYo. .oPYo. 8      o8YooP' 8    8 o8YooP' 
8 `b 8 8    8  8 8    ' 8oooo8 8   oo  8   `b 8    8  8   `b 
8  `b8 8    8  8 8    . 8.     8    8  8    8 8    8  8    8 
8   `8 `YooP'  8 `YooP' `Yooo' `YooP8  8    8 `YooP'  8oooP' 
..:::..:.....::..:.....::.....::....8 :..:::..:.....::......:
:::::::: @1337kid ::::::::::::::::::8 ::::::: v1.1 ::::::::::'''

def menu():
	return '''
Select a preset
~~~~~~~~~~~~~~
[1] Chocolate	    [4] TheSky
[2] Lightlime	    [5] VioBlue
[3] Noice (Special) [6] Wildfire
~~~~~~~~~~~~~~~~~~~~~~~~~~~~
[0] Custom
	'''

def get_preset(name):
	data=toml.load(open(f'./presets/{name}.toml'))
	return [data['background'],data['theme']]
#=============================================================
def generate_background(primary,secondary):
	svg_temp=xmltodict.parse(open('template/background.svg').read())
	svg_temp['svg']['defs']['linearGradient']['stop'][0]['@stop-color']=primary
	svg_temp['svg']['defs']['linearGradient']['stop'][1]['@stop-color']=secondary
	open('temp.svg','w').write(xmltodict.unparse(svg_temp))
	cairosvg.svg2png(url='temp.svg', write_to=f'./export/background.png')
	os.remove('temp.svg')

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
		if name=='noice':
			cairosvg.svg2png(url='template/noice.svg', write_to='./export/background.png')
			export_selection_png(data[0]['selection_bg_colour'])
			export_theme_config(data[1]['font_colour'],data[1]['selection_font_colour'],data[1]['label_colour'])
			print(Fore.GREEN + f"~ Generated theme saved to {os.getcwd()+'/export/'}" + Style.RESET_ALL)
			return
	if custom:
		data=custom
	generate_background(data[0]['primary'],data[0]['secondary'])
	export_selection_png(data[0]['selection_bg_colour'])
	export_theme_config(data[1]['font_colour'],data[1]['selection_font_colour'],data[1]['label_colour'])
	print(Fore.GREEN + f"~ Generated theme saved to {os.getcwd()+'/export/'}" + Style.RESET_ALL)