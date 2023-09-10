### Create Your Own Preset
NoiceGRUB preset files have the syntax of TOML and ends with `.toml` extension. Your own preset shall be placed in `presets` folder. It will be shown in the preset menu when you execute `NoiceGRUB.py`
#### File format
```toml
template='template name here'

# This section is mandatory and defines background.png file
[background]
primary="primary gradient colour"
secondary="secondary gradient colour"
header_font_colour = "header font colour or 'BOOTMENU' text colour"
footer_font_colour = "footer font colour or GRUB keymap text colour"
selection_bg_colour = "backgound colour of selection highlighter"

# This section defines theme.txt file and is mandatory too
[theme]
font_colour = "#000"
selection_font_colour = "#d0c4f5"
label_colour = "#d0c4f5"

# This section is optional and it depends on the template
[extra]
```
#### Noice template extra section
```toml
[extra]
menuboxbg=["menu box background colour"]
polygon=["primary gradeint colour of topright polygon","secondary gradient colour"]
ellipse=["primary gradeint colour of bottomright eliipse","secondary gradient colour"]
circle=["primary gradeint colour of topleft circle","secondary gradient colour"]
triangle=["background colour of bottom left triangle"]
```
#### TheMan template extra section
```toml
[extra]
centreleftlines=["centre-left lines, primary gradient colour","secondary gradient colour","tertiary gradient colour"]
bottomrightlines=["bottomright lines, primary gradient colour","secondary gradient colour"]
man=["primary gradient colour of the man","secondary gradient colour"]
polygon=["colour of bottomleft polygon"]
hexagon=["colour of topright hexagon"]
```
#### Mountains template extra section
```toml
[extra]
menubox=['menubox background colour']
mountains=["primary gradient colour of the mountain","secondary gradient colour"]
circle=["primary gradient colour of topleft circle","secondary gradient colour"]
```