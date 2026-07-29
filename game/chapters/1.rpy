label version_01:

    narrator "[ VERSION 0.1 - The Prototype ]"
    narrator "The world contains:"
    narrator "One bakery. One road. One tree. One customer. One best friend."
    narrator "Her name is Mina."

    $ loop_count = 0

    label prototype_loop:

        $ loop_count += 1

        if loop_count == 1:
            narrator "She arrives at exactly the same time she always does."
            mina "Good morning!"
            eli "Morning!"
            mina "Busy today?"
            eli "Always!"
            mina "See you tomorrow."
            narrator "She leaves, the door closes."
            narrator "The bell above it rings exactly twice."
            narrator "It always rings exactly twice."

        elif loop_count == 2:
            narrator "The next day.. identical."
            mina "Good morning!"
            eli "Morning!"
            mina "Busy today?"
            eli "Always!"
            narrator "You notice her smile doesn't quite reach her eyes today."
            narrator "Or maybe it never did."
            narrator "You can't remember."
            mina "See you tomorrow."

        elif loop_count == 3:
            narrator "The third day."
            narrator "You already know what she's going to sat."
            mina "Good morning!"

            menu:
                "Morning!":
                    eli "Morning!"
                    $ glitch_clicks += 1
                "..Do you ever feel like we've had this conversation before?":
                    $ glitch_clicks += 2
                    $ eli_awareness += 1
                    eli "..Do you ever feel like we've had this conversation before?"
                    mina "What do you mean?"
                    narrator "She tilts her head and something flickers behind her eyes."
                    narrator "Just for a monent."
                    mina "Every morning is a new morning, Eli."
                    narrator "She says it like she's reading it."
            
            mina "Busy today?"
            eli "Always!"

            if flitch_clicks >= 2:
                mina "See you after the next upd-"
                pause 0.5
                narrator "She stops."
                narrator "Her mouth closes."
                narrator "Opens again."
                mina "..See you tomorrow."
                narrator "She blinks twice, and corrects herself."
                narrator "The bell rings twice twice."
                narrator "You stand very still."
                narator "You don't know why your hands are shaking."
            else:
                mina "See you tomorrow."

        if loop_count < 3:
            jump prototype_loop
        else:
            jump version_02