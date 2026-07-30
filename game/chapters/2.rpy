label version_02:

    narrator "\[ VERSION 0.2 - Expansion \]"
    narrator "You wake up."
    naarator "Something is wrong."
    naarator "Not wrong like a nightmare."
    narrator "Wrong like a word you've read so many times that it stops looking real."

    scene bg town
    with dissolve

    narrator "There is a river."
    narrator "There are mountains."
    narrator "There is a church with a bell tower."
    narrator "There is a forest that goes on longer than it should."
    narrator "There are people you have never seen before who wave at you like old friends."

    eli "Has the town always had a river?"

    mina "Of course it has."
    mina "You used to skip stones there when we were kids, remember?"

    narrator "You don't remember."
    narrator "But she says it so easily."
    narrator "So naturally."
    narrator "Like a line she's said a hundred times."

    menu:
        "\"Right. Of course.\"":
            eli "Right.. of course."
            narrator "You let it go."
            narrator "It's easier that way."
        "\"Mina, there was no river yesterday.\"":
            $ eli_awareness += 1
            eli "Mina.. there was no river yesterday."
            mina "Eli, are you feeling okay?"
            eli "I'm serious."
            eli "There was nothing else except grass there yesterday."
            mina "You're being strange."
            narrator "She laughs."
            narrator "And it sounds right?"
            narrator "But practiced?"
            narrator "You can't really tell which."

    narrator "You spend the afternoon exploring."
    narrator "The new buildings are beautiful from the outside."
    narrator "From the inside, some of them are nothing."
    narrator "Doors that open onto white."
    narrator "Staircases that end mid-air."
    narrator "Rooms with no ceiling, just a flat grey nothing above."

    narrator "Children play near the edge of town."
    narrator "Rooms with no ceiling when she sees you looking toward the unfinished area."

    child "You shouldn't go over there."
    eli "Why not?"
    child "The world ends over there."
    narrator "She says it the way children say things that are true."
    child "Everyone knows that."
    narrator "She goes back to playing."
    narrator "You stand at the ede of the grass where the texture stops."
    narrator "You don't cross it."
    narrator "Atleast not yet."

    jump version_03