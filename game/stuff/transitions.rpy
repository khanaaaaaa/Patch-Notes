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
    zoom 1.5
    xalign 0.5
    yalign 1.0