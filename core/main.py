import xmltodict,cairosvg,os,toml
from colorama import Fore, Style
from core.templateconf import *
import re


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

def generate_background(template,background_props,extra=None):
	svg_temp=xmltodict.parse(open(f'template/{template}.svg').read())
	#=== header & footer font colour
	svg_temp['svg']['path'][header_footer_placement[template][0]]['@fill']=background_props[2]
	svg_temp['svg']['path'][header_footer_placement[template][1]]['@fill']=background_props[3]
	#===
	if template=='Kewl':   # For Kewl Template
		svg_temp['svg']['defs']['linearGradient']['stop'][0]['@stop-color']=background_props[0]
		svg_temp['svg']['defs']['linearGradient']['stop'][1]['@stop-color']=background_props[1]
	elif template=='Noice':# For Noice Template
		# Background Gradient
		svg_temp['svg']['defs']['linearGradient'][0]['stop'][0]['@stop-color']=background_props[0]
		svg_temp['svg']['defs']['linearGradient'][0]['stop'][1]['@stop-color']=background_props[1]
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
	elif template=='TheMan':# For TheMan template
		# Background Gradient
		svg_temp['svg']['defs']['linearGradient'][0]['stop'][0]['@stop-color']=background_props[0]
		svg_temp['svg']['defs']['linearGradient'][0]['stop'][1]['@stop-color']=background_props[1]
		# CentreLeft lines linear gradient
		svg_temp['svg']['defs']['linearGradient'][1]['stop'][0]['@stop-color']=extra['centreleftlines'][0]
		svg_temp['svg']['defs']['linearGradient'][1]['stop'][1]['@stop-color']=extra['centreleftlines'][1]
		svg_temp['svg']['defs']['linearGradient'][1]['stop'][2]['@stop-color']=extra['centreleftlines'][2]
		# Bottomright lines linear gradient
		svg_temp['svg']['defs']['linearGradient'][2]['stop'][0]['@stop-color']=extra['bottomrightlines'][0]
		svg_temp['svg']['defs']['linearGradient'][2]['stop'][1]['@stop-color']=extra['bottomrightlines'][1]
		# Man - linear gradient
		svg_temp['svg']['defs']['linearGradient'][3]['stop'][0]['@stop-color']=extra['man'][0]
		svg_temp['svg']['defs']['linearGradient'][3]['stop'][1]['@stop-color']=extra['man'][1]
		# bottomleft polygon
		svg_temp['svg']['defs']['linearGradient'][4]['stop'][0]['@stop-color']=extra['polygon'][0]
		svg_temp['svg']['defs']['linearGradient'][4]['stop'][1]['@stop-color']=extra['polygon'][0]
		# hexagon colour
		svg_temp['svg']['path'][3]['@fill']=extra['hexagon'][0]
	open('temp.svg','w').write(xmltodict.unparse(svg_temp,pretty=True))
	'''
	When unparsing, xmltodict changes the order of elements.
	The below code is to keep <rect> tag of menubox in its place
	'''
	data=open('temp.svg').readlines()
	menu_box=data.pop(menu_box_placement[template][0]) 
	data.insert(menu_box_placement[template][1],menu_box)
	open('temp.svg','w').writelines(data)
	#=============
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
	if custom:
		data=custom
	#=====
	background_props=[data[1]['primary'],data[1]['secondary'],data[1]['header_font_colour'],data[1]['footer_font_colour']]
	#=====
	if data[0]=='Kewl':
		generate_background('Kewl',background_props)
	else:
		generate_background(data[0],background_props,data[3])
	export_selection_png(data[1]['selection_bg_colour'])
	export_theme_config(data[2]['font_colour'],data[2]['selection_font_colour'],data[2]['label_colour'])
	print(Fore.GREEN + f"~ Generated theme saved to {os.getcwd()+'/export/'}" + Style.RESET_ALL)