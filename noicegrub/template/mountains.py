from noicegrub.template import NgCommonProps

class NgMountainsTemplate(NgCommonProps):
    def __init__(self,preset):
        super().__init__(preset)
        self.template = 'Mountains'
        self.extra_props = preset[3]
        
        self.set_common_props()

        # menubox background colour
        self.svg_temp['svg']['path'][3]['@fill']=self.extra_props['menubox'][0]
        # Bottom mountains gradient
        self.svg_temp['svg']['defs']['linearGradient'][1]['stop'][0]['@stop-color']=self.extra_props['mountains'][0]
        self.svg_temp['svg']['defs']['linearGradient'][1]['stop'][1]['@stop-color']=self.extra_props['mountains'][1]
        # Topleft circle gradient
        self.svg_temp['svg']['defs']['linearGradient'][2]['stop'][0]['@stop-color']=self.extra_props['circle'][0]
        self.svg_temp['svg']['defs']['linearGradient'][2]['stop'][1]['@stop-color']=self.extra_props['circle'][1]