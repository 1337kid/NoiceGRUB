import os
import xmltodict
import cairosvg
from noicegrub.templateconf import header_footer_placement,menu_box_placement

class NgCommonProps():
    def __init__(self,preset):
        self.template = 'Kewl'
        self.common_props = preset[1]
        self.theme_txt_conf = preset[2]
        
        self.set_common_props()
        
    def set_common_props(self):
        self.svg_temp=xmltodict.parse(open(f'template/{self.template}.svg').read())
        #==== header & footer colours
        self.svg_temp['svg']['path'][header_footer_placement[self.template][0]]['@fill']=self.common_props['header_font_colour']
        self.svg_temp['svg']['path'][header_footer_placement[self.template][1]]['@fill']=self.common_props['footer_font_colour']
        #==== background gradient
        if self.template == 'Kewl':
            self.svg_temp['svg']['defs']['linearGradient']['stop'][0]['@stop-color']=self.common_props['primary']
            self.svg_temp['svg']['defs']['linearGradient']['stop'][1]['@stop-color']=self.common_props['secondary']
        else:
            self.svg_temp['svg']['defs']['linearGradient'][0]['stop'][0]['@stop-color']=self.common_props['primary']
            self.svg_temp['svg']['defs']['linearGradient'][0]['stop'][1]['@stop-color']=self.common_props['secondary']

    def export_theme(self):
        if not os.path.exists('export'):
            os.mkdir('export')
        #============ background.png
        open('temp.svg','w').write(xmltodict.unparse(self.svg_temp,pretty=True))
        '''
        When unparsing, xmltodict changes the order of elements.
        The below code is to keep <rect> tag of menubox in its place
        '''
        data=open('temp.svg').readlines()
        menu_box=data.pop(menu_box_placement[self.template][0]) 
        data.insert(menu_box_placement[self.template][1],menu_box)
        open('temp.svg','w').writelines(data)

        png=cairosvg.svg2png(url='temp.svg')
        open('./export/background.png','wb').write(png)
        os.remove('temp.svg')
        #============ menu box selection background colour
        filenames=['select_c','select_e','select_w']
        for i in filenames:
            svg_temp=xmltodict.parse(open(f'template/{i}.svg').read())
            svg_temp['svg']['path']['@fill']=self.common_props['selection_bg_colour']
            open('temp.svg','w').write(xmltodict.unparse(svg_temp))
            cairosvg.svg2png(url='temp.svg', write_to=f'./export/{i}.png')
            os.remove('temp.svg')
        #============ theme.txt config file
        font_colour,selection_font_colour,label_colour = self.theme_txt_conf['font_colour'],self.theme_txt_conf['selection_font_colour'],self.theme_txt_conf['label_colour']
        config=open('template/theme.txt').read()
        config=config.replace('{font_colour}',f'"{font_colour}"')
        config=config.replace('{selection_font_colour}',f'"{selection_font_colour}"')
        config=config.replace('{label_colour}',f'"{label_colour}"')
        open('./export/theme.txt','w').write(config)