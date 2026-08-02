label version_02:

    narrator "\[ VERSION 0.2 - Expansion \]"
    narrator "You wake up."
    narrator "Something is wrong."
    narrator "Not wrong like a nightmare."
    narrator "Wrong like a word you've read so many times that it stops looking real."

    scene bg town
    with dissolve

    narrator "There is a river."
    narrator "There are mountains."
    narrator "There is a church with a bell tower."
    narrator "There is a forest that goes on longer than it should."
    narrator "There are people you have never seen before who wave at you like old friends."

    show minaneutralquiet at center_char
    eli "Has the town always had a river?"
    hide minaneutralquiet
    show minasmiletalk at center_char
    mina "Of course it has."
    mina "You used to skip stones there when we were kids, remember?"
    hide minasmiletalk
    show minaneutralquiet at center_char
    narrator "You don't remember."
    narrator "But she says it so easily."
    narrator "So naturally."
    narrator "Like a line she's said a hundred times."

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
            narrator "She laughs."
            narrator "And it sounds right?"
            narrator "But practiced?"
            narrator "You can't really tell which."
            hide minaneutralquiet

    narrator "You spend the afternoon exploring."
    narrator "The new buildings are beautiful from the outside."
    narrator "From the inside, some of them are nothing."
    narrator "Doors that open onto white."
    narrator "Staircases that end mid-air."
    narrator "Rooms with no ceiling, just a flat grey nothing above."

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
    narrator "You stand at the edge of the grass where the texture stops."
    narrator "You don't cross it."
    narrator "Atleast not yet."
    hide childquiet

    jump version_03