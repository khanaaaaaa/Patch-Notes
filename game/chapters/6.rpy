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

    narrator "You wake up. Something is different — the air, the light, the silence."

    scene bg room
    with dissolve

    narrator "You go to Mina's house. There is no Mina's house. There is a field."
    narrator "There has always been a field."

    scene bg field
    with dissolve

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

    narrator "You ask everyone. The baker, the children, the NPCs from version 0.2."
    narrator "Nothing. Not a flicker. Just blank, comfortable nothing."

    narrator "You go to the field. Stand where her door used to be."
    narrator "The grass is perfect. Undisturbed. Like she was never there."

    narrator "In the grass. Half-hidden. A notebook."
    narrator "Not yours. Hers."
    narrator "The developer forgot to delete one prop."

    narrator "The first pages are full of her handwriting — the versions, the rewrites, the people who disappeared."
    narrator "About you. She wrote about you."

    narrator "The last page."
    narrator "One sentence."
    narrator "\"If you're reading this... I lost.\""

    pause 2.0

    narrator "You sit in the field for a long time. The sun moves."
    narrator "Nobody comes to find you. Nobody knows how to."

    $ notebook_entries.append("mina's notebook. found it in the field where her house was. last page just says 'if you're reading this... i lost.'")
    $ show_notebook_icon = True

    jump version_07
