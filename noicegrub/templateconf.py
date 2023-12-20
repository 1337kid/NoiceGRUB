from math import floor

item_placement={
    'Kewl':[4,6],
    'Noice':[3,9],
    'TheMan':[3,7],
    'Mountains':[5,5],
    'Nico':[5,6]
}
header_footer_placement={
    'Kewl':[1,0],
    'Noice':[5,3],
    'TheMan':[6,5],
    'Mountains':[1,4],
    'Nico':[None,None],
}

def calc_selection_scale(font_size):
    height = 30.0
    def_fontsize = 16.0
    new_height = float(font_size)*(height/def_fontsize)
    size = floor(new_height/height)
    return (new_height, size)