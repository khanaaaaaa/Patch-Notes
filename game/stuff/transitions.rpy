default loop_count = 0
default mina_exists = True
default notebook_entries = []
default glitch_clicks = 0

transform bg_fit:
    xysize (config.screen_width, config.screen_height)

transform center_char:
    zoom 1.5
    xalign 0.5
    yalign 1.0