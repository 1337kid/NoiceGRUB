from noicegrub.template import NgCommonProps

class NgNicoTemplate(NgCommonProps):
    def __init__(self,preset):
        super().__init__(preset)
        self.template = 'Nico'
        self.extra_props = preset[3]
        
        self.set_common_props()

        # menubox background colour
        self.svg_temp['svg']['path'][2]['@fill']=self.extra_props['menubox'][0]
        # Header text font colour (gradient)
        self.svg_temp['svg']['defs']['linearGradient'][1]['stop'][0]['@stop-color']=self.extra_props['header_text_gradient'][0]
        self.svg_temp['svg']['defs']['linearGradient'][1]['stop'][1]['@stop-color']=self.extra_props['header_text_gradient'][1]