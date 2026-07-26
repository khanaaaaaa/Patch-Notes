label version_01:

    narrator "[ VERSION 0.1 - The Prototype ]"
    narrator "The world contains:"
    narrator "One bakery. One road. One tree. One customer. One best friend."

    $ loop_count = 0

    label prototype_loop:

        $ loop_count += 1

        mina "Good morning!"
        eli "Morning!"
        mina "Busy today?"
        eli "Always!"

        if loop count >= 3:
            $ glitch_click += 1

        if glitch_clicks >= 2:
            mina "See you after the next upd-"
            mina "...See you tomorrow."
            narrator "She blinks."
            narrator "Corrects herself."
            narrator "Nobody notices."
        else: 
            mina "See you tomorrow."

        if loop_count < 3:
            jump prototype_loop
        else:
            jump version_02git