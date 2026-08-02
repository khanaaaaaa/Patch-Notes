label version_02:

    narrator "\[ VERSION 0.2 - Expansion \]"
    narrator "Something is wrong."
    narrator "Not wrong like a nightmare. Wrong like a word you've read so many times it stops looking real."

    scene bg town
    with dissolve

    narrator "There's a river now. Mountains. A church. A forest that goes on longer than it should."
    narrator "People you've never seen wave at you like old friends."

    show minaneutralquiet at center_char
    eli "Has the town always had a river?"
    hide minaneutralquiet
    show minasmiletalk at center_char
    mina "Of course it has."
    mina "You used to skip stones there when we were kids, remember?"
    hide minasmiletalk
    show minaneutralquiet at center_char
    narrator "You don't remember."
    narrator "But she says it so easily. Like a line she's said a hundred times."

    menu:
        "\"Right. Of course.\"":
            eli "Right.. of course."
            narrator "You let it go."
            narrator "It's easier that way."
            hide minaneutralquiet
        "\"Mina, there was no river yesterday.\"":
            $ eli_awareness += 1
            eli "Mina.. there was no river yesterday."
            hide minaneutralquiet
            show minasmiletalk at center_char
            mina "Eli, are you feeling okay?"
            hide minasmiletalk
            show minaneutralquiet at center_char
            eli "I'm serious."
            eli "There was nothing else except grass there yesterday."
            hide minaneutralquiet
            show minasmiletalk at center_char
            mina "You're being strange."
            hide minasmiletalk
            show minaneutralquiet at center_char
            narrator "She laughs. It sounds right. Maybe practiced. You can't tell."
            hide minaneutralquiet

    narrator "The new buildings are beautiful outside. Inside, some are nothing."
    narrator "Doors that open onto white. Staircases that end mid-air. Rooms with no ceiling, just flat grey above."

    narrator "Children play near the edge of town."
    narrator "A child stops when she sees you looking toward the unfinished area."

    show childtalk at center_char
    child "You shouldn't go over there."
    hide childtalk
    show childquiet at center_char
    eli "Why not?"
    hide childquiet
    show childtalk at center_char
    child "The world ends over there."
    hide childtalk
    show childquiet at center_char
    narrator "She says it the way children say things that are true."
    hide childquiet
    show childtalk at center_char
    child "Everyone knows that."
    hide childtalk
    show childquiet at center_char
    narrator "She goes back to playing."
    narrator "You stand where the texture stops. You don't cross it."
    hide childquiet

    jump version_03