from noicegrub.theme import NgCommonProps

class NgNoiceTemplate(NgCommonProps):
    def __init__(self,preset):
        super().__init__(preset)
        self.template = 'Noice'
        self.extra_props = preset[3]
        
    def set_extra_props(self):
        self.svg_temp['svg']['rect'][1]['@fill']=self.extra_props['menuboxbg'][0]
        # Topright Polygon gradient
        self.svg_temp['svg']['defs']['linearGradient'][1]['stop'][0]['@stop-color']=self.extra_props['polygon'][0]
        self.svg_temp['svg']['defs']['linearGradient'][1]['stop'][1]['@stop-color']=self.extra_props['polygon'][1]
        # Bottomright ellipse gradient
        self.svg_temp['svg']['defs']['linearGradient'][2]['stop'][0]['@stop-color']=self.extra_props['ellipse'][0]
        self.svg_temp['svg']['defs']['linearGradient'][2]['stop'][1]['@stop-color']=self.extra_props['ellipse'][1]
        # Topleft quarter circle gradient
        self.svg_temp['svg']['defs']['linearGradient'][3]['stop'][0]['@stop-color']=self.extra_props['circle'][0]
        self.svg_temp['svg']['defs']['linearGradient'][3]['stop'][1]['@stop-color']=self.extra_props['circle'][1]
        # Bottomleft triangle colour
        self.svg_temp['svg']['path'][0]['@fill']=self.extra_props['triangle'][0]