label version_01:

    narrator "\[ VERSION 0.1 - The Prototype \]"
    narrator "One bakery. One road. One tree. One customer."
    narrator "Her name is Mina."

    $ loop_count = 0

    label prototype_loop:

        $ loop_count += 1

        if loop_count == 1:
            scene bg town
            narrator "She arrives at the same time she always does. You've never checked a clock to confirm this. You just know."
            show minasmiletalk at center_char
            mina "Morning!"
            hide minasmiletalk
            show minaneutralquiet at center_char
            eli "Morning."
            hide minaneutralquiet
            show minasmiletalk at center_char
            mina "Busy?"
            hide minasmiletalk
            show minaneutralquiet at center_char
            eli "When am I not."
            hide minaneutralquiet
            show minasmiletalk at center_char
            mina "See you tomorrow."
            hide minasmiletalk
            show minaneutralquiet at center_char
            narrator "The door. The bell. Twice."
            narrator "You count without meaning to."
            hide minaneutralquiet

        elif loop_count == 2:
            narrator "The next day arrives the way the next day always does — without asking."
            show minasmiletalk at center_char
            mina "Morning!"
            hide minasmiletalk
            show minaneutralquiet at center_char
            eli "Morning."
            hide minaneutralquiet
            show minasmiletalk at center_char
            mina "Busy?"
            hide minasmiletalk
            show minaneutralquiet at center_char
            eli "When am I not."
            narrator "Something about her smile is off. Not wrong, exactly. More like a copy of itself."
            hide minaneutralquiet
            show minasmiletalk at center_char
            mina "See you tomorrow."
            hide minasmiletalk

        elif loop_count == 3:
            narrator "By the third day you know the shape of it before it starts."
            narrator "You open your mouth before she does."
            show minasmiletalk at center_char
            mina "Morning!"
            hide minasmiletalk
            show minaneutralquiet at center_char

            menu:
                "Morning.":
                    eli "Morning."
                    $ glitch_clicks += 1
                "..Have we done this before?":
                    $ glitch_clicks += 2
                    $ eli_awareness += 1
                    eli "Have we done this before?"
                    hide minaneutralquiet
                    show minasmiletalk at center_char
                    mina "Done what?"
                    hide minasmiletalk
                    show minaneutralquiet at center_char
                    narrator "She tilts her head. There's a half-second where her face does nothing at all."
                    hide minaneutralquiet
                    show minasmiletalk at center_char
                    mina "Every morning is a new morning, Eli."
                    hide minasmiletalk
                    show minaneutralquiet at center_char
                    narrator "The words are right. The cadence is wrong. Like she learned the sentence phonetically."

            hide minaneutralquiet
            show minasmiletalk at center_char
            mina "Busy?"
            hide minasmiletalk
            show minaneutralquiet at center_char
            eli "When am I not."

            if glitch_clicks >= 2:
                hide minaneutralquiet
                show minasmiletalk at center_char
                mina "See you after the next upd-"
                hide minasmiletalk
                show minaneutralquiet at center_char
                narrator "She stops mid-word. Her mouth stays open a moment, like she's listening for something."
                hide minaneutralquiet
                show minasmiletalk at center_char
                mina "..See you tomorrow."
                hide minasmiletalk
                show minaneutralquiet at center_char
                narrator "The bell rings twice. You don't move."
                narrator "Your hands are shaking and you have no idea why."
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