label version_06:

    narrator "\[ VERSION 0.6 - Performance Patch \]"
    pause 1.0

    narrator "Patch Notes:"
    pause 0.5
    narrator " - Removed unnecessary NPC."
    pause 0.5
    narrator " - Improved memory usage."
    pause 0.5
    narrator " - General stability improvements."
    pause 1.5

    scene bg black
    with dissolve

    narrator "You wake up."
    narrator "Something is different."
    narrator "The air is different."
    narrator "The light is different."
    narrator "The silence is different."

    scene bg room
    with dissolve

    narrator "You go to Mina's house."
    narrator "There is no Mina's house."
    narrator "There is a field."
    narrator "There has always been a field."

    $ show_notebook_icon = False

    show mayorsmilequiet at center_char
    eli "Where is Mina?"
    hide mayorsmilequiet
    show mayorneutraltalk at center_char
    mayor "Who?"
    hide mayorneutraltalk
    show mayorneutralquiet at center_char
    eli "Mina. She lives- she lived on Birch Street."
    hide mayorneutralquiet
    show mayorneutraltalk at center_char
    mayor "There's no one by that name here, son."
    hide mayorneutraltalk
    show mayorneutralquiet at center_char
    eli "She was my best friend."
    hide mayorneutralquiet
    show mayorneutraltalk at center_char
    mayor "Are you feeling alright?"
    hide mayorneutraltalk

    narrator "You ask everyone."
    narrator "The baker.. the children.. the new NPCs who appeared in version 0.2."
    narrator "Nobody."
    narrator "Not a flicker of recognition."
    narrator "Not a hesitation."
    narrator "Just blank, comfortable nothing."

    narrator "You go to the field."
    narrator "You stand where her door used to be."
    narrator "The grass is perfect."
    narrator "Undisturbed."
    narrator "Like she was never there."

    narrator "Except."
    narrator "In the grass."
    narrator "Half-hidden."
    narrator "A notebook."

    narrator "Not yours."
    narrator "Hers."

    narrator "The developer forgot to delete one prop."

    narrator "You open it."
    narrator "The first pages are full of her handwriting."
    narrator "Notes about the versions.. about the rewrites.. about the people who disappeared."
    narrator "About you."
    narrator "She wrote about you."

    narrator "The last page."
    narrator "One sentence."
    narrator "\"If you're reading this... I lost.\""

    pause 2.0

    narrator "You sit in the field for a long time."
    narrator "The sun moves."
    narrator "Nobody comes to find you."
    narrator "Nobody knows how to."

    $ notebook_entries.append("Mina's notebook. Last line: 'If you're reading this... I lost.'")
    $ show_notebook_icon = True

    jump version_07
