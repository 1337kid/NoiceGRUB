from noicegrub.template import NgCommonProps

class NgTheManTemplate(NgCommonProps):
    def __init__(self,preset):
        super().__init__(preset)
        self.template = 'TheMan'
        self.extra_props = preset[3]
        
    def set_extra_props(self):
        # CentreLeft lines linear gradient
        self.svg_temp['svg']['defs']['linearGradient'][1]['stop'][0]['@stop-color']=self.extra_props['centreleftlines'][0]
        self.svg_temp['svg']['defs']['linearGradient'][1]['stop'][1]['@stop-color']=self.extra_props['centreleftlines'][1]
        self.svg_temp['svg']['defs']['linearGradient'][1]['stop'][2]['@stop-color']=self.extra_props['centreleftlines'][2]
        # Bottomright lines linear gradient
        self.svg_temp['svg']['defs']['linearGradient'][2]['stop'][0]['@stop-color']=self.extra_props['bottomrightlines'][0]
        self.svg_temp['svg']['defs']['linearGradient'][2]['stop'][1]['@stop-color']=self.extra_props['bottomrightlines'][1]
        # Man - linear gradient
        self.svg_temp['svg']['defs']['linearGradient'][3]['stop'][0]['@stop-color']=self.extra_props['man'][0]
        self.svg_temp['svg']['defs']['linearGradient'][3]['stop'][1]['@stop-color']=self.extra_props['man'][1]
        # bottomleft polygon
        self.svg_temp['svg']['defs']['linearGradient'][4]['stop'][0]['@stop-color']=self.extra_props['polygon'][0]
        self.svg_temp['svg']['defs']['linearGradient'][4]['stop'][1]['@stop-color']=self.extra_props['polygon'][0]
        # hexagon colour
        self.svg_temp['svg']['path'][3]['@fill']=self.extra_props['hexagon'][0]