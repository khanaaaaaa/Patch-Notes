default loop_count = 0
default mina_exists = True
default notebook_entries = []
default glitch_clicks = 0
default eli_awareness = 0
default mina_trust = 0
default chose_to_remember = False
default show_notebook_icon = False

transform bg_fit:
    xysize (config.screen_width, config.screen_height)

transform center_char:
    xalign 0.5
    yalign 1.0
    zoom 1.7

transform left_char:
    xalign 0.15
    yalign 1.0

transform right_char:
    xalign 0.85
    yalign 1.0

transform char_fadein:
    alpha 0.0
    linear 0.4 alpha 1.0

transform char_fadeout:
    alpha 1.0
    linear 0.4 alpha 0.0

transform shake:
    xoffset 0
    linear 0.04 xoffset -12
    linear 0.04 xoffset 12
    linear 0.04 xoffset -8
    linear 0.04 xoffset 8
    linear 0.04 xoffset -4
    linear 0.04 xoffset 4
    linear 0.04 xoffset 0

transform shake_hard:
    xoffset 0
    linear 0.03 xoffset -20
    linear 0.03 xoffset 20
    linear 0.03 xoffset -16
    linear 0.03 xoffset 16
    linear 0.03 xoffset -10
    linear 0.03 xoffset 10
    linear 0.03 xoffset -5
    linear 0.03 xoffset 5
    linear 0.03 xoffset 0

transform glitch_flicker:
    alpha 1.0
    linear 0.05 alpha 0.0
    linear 0.05 alpha 1.0
    linear 0.03 alpha 0.0
    linear 0.03 alpha 1.0
    pause 0.1
    linear 0.05 alpha 0.0
    linear 0.05 alpha 1.0

define slow_fade = Fade(2.0, 0.0, 2.0)
define very_slow_fade = Fade(3.0, 0.5, 3.0)
define flash_white = Fade(0.1, 0.0, 0.5, color="#ffffff")
define flash_black = Fade(0.1, 0.0, 0.8, color="#000000")
define slow_dissolve = Dissolve(1.5)
define fast_dissolve = Dissolve(0.2)

define narrator_nvl = Character(None, kind=nvl)