label version_01:

    narrator "\[ VERSION 0.1 - The Prototype \]"
    narrator "One bakery. One road. One tree. One customer."
    narrator "Her name is Mina."

    $ loop_count = 0

    label prototype_loop:

        $ loop_count += 1

        if loop_count == 1:
            scene bg town
            narrator "She arrives at exactly the same time she always does."
            show minasmiletalk at center_char
            mina "Good morning!"
            hide minasmiletalk
            show minaneutralquiet at center_char
            eli "Morning!"
            hide minaneutralquiet
            show minasmiletalk at center_char
            mina "Busy today?"
            hide minasmiletalk
            show minaneutralquiet at center_char
            eli "Always!"
            hide minaneutralquiet
            show minasmiletalk at center_char
            mina "See you tomorrow."
            hide minasmiletalk
            show minaneutralquiet at center_char
            narrator "The door closes. The bell rings twice."
            narrator "It always rings twice."
            hide minaneutralquiet

        elif loop_count == 2:
            narrator "The next day. Identical."
            show minasmiletalk at center_char
            mina "Good morning!"
            hide minasmiletalk
            show minaneutralquiet at center_char
            eli "Morning!"
            hide minaneutralquiet
            show minasmiletalk at center_char
            mina "Busy today?"
            hide minasmiletalk
            show minaneutralquiet at center_char
            eli "Always!"
            narrator "Her smile doesn't reach her eyes today."
            narrator "Or maybe it never did."
            hide minaneutralquiet
            show minasmiletalk at center_char
            mina "See you tomorrow."
            hide minasmiletalk

        elif loop_count == 3:
            narrator "The third day."
            narrator "You already know what she's going to say."
            show minasmiletalk at center_char
            mina "Good morning!"
            hide minasmiletalk
            show minaneutralquiet at center_char

            menu:
                "Morning!":
                    eli "Morning!"
                    $ glitch_clicks += 1
                "..Do you ever feel like we've had this conversation before?":
                    $ glitch_clicks += 2
                    $ eli_awareness += 1
                    eli "..Do you ever feel like we've had this conversation before?"
                    hide minaneutralquiet
                    show minasmiletalk at center_char
                    mina "What do you mean?"
                    hide minasmiletalk
                    show minaneutralquiet at center_char
                    narrator "She tilts her head. Something flickers behind her eyes."
                    hide minaneutralquiet
                    show minasmiletalk at center_char
                    mina "Every morning is a new morning, Eli."
                    hide minasmiletalk
                    show minaneutralquiet at center_char
                    narrator "She says it like she's reading it."
            
            hide minaneutralquiet
            show minasmiletalk at center_char
            mina "Busy today?"
            hide minasmiletalk
            show minaneutralquiet at center_char
            eli "Always!"

            if glitch_clicks >= 2:
                hide minaneutralquiet
                show minasmiletalk at center_char
                mina "See you after the next upd-"
                hide minasmiletalk
                show minaneutralquiet at center_char
                narrator "She stops. Mouth closes. Opens again."
                hide minaneutralquiet
                show minasmiletalk at center_char
                mina "..See you tomorrow."
                hide minasmiletalk
                show minaneutralquiet at center_char
                narrator "The bell rings twice. You don't move."
                narrator "You don't know why your hands are shaking."
                hide minaneutralquiet
            else:
                hide minaneutralquiet
                show minasmiletalk at center_char
                mina "See you tomorrow."
                hide minasmiletalk

        if loop_count < 3:
            jump prototype_loop
        else:
            jump version_02