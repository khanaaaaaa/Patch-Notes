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

    narrator "You wake up. The quality of the light is different. The silence has a different texture."

    scene bg room
    with dissolve

    narrator "You go to Mina's house."
    narrator "There is no Mina's house."
    narrator "There is a field. There has always been a field."

    scene bg field
    with dissolve

    $ show_notebook_icon = False

    show mayorsmilequiet at center_char
    eli "Where is Mina?"
    hide mayorsmilequiet
    show mayorneutraltalk at center_char
    mayor "I'm sorry?"
    hide mayorneutraltalk
    show mayorneutralquiet at center_char
    eli "Mina. She lived on Birch Street."
    hide mayorneutralquiet
    show mayorneutraltalk at center_char
    mayor "There's no one by that name here, son."
    hide mayorneutraltalk
    show mayorneutralquiet at center_char
    eli "She was my best friend."
    hide mayorneutralquiet
    show mayorneutraltalk at center_char
    mayor "Are you feeling well?"
    hide mayorneutraltalk

    narrator "You ask everyone. The baker. The children. The people who appeared in version 0.2 and waved at you like old friends."
    narrator "Nothing. Not a hesitation. Just the smooth, untroubled faces of people who have never heard the name."

    narrator "You go to the field. Stand where her door was."
    narrator "The grass is perfect. No indent, no worn path, no sign."

    narrator "Except."
    narrator "Half-hidden in the grass. A notebook."
    narrator "Not yours."

    narrator "The developer forgot to delete one prop."

    narrator "Her handwriting fills the first pages. The versions. The rewrites. The names of people who got removed."
    narrator "And then, near the back, pages about you."
    narrator "She'd been watching you notice things. Writing it down."

    narrator "The last page has one line."
    narrator "\"If you're reading this, I lost.\""

    pause 2.0

    narrator "You sit in the field until the light changes."
    narrator "No one comes to find you. No one knows to.

    $ notebook_entries.append("mina's notebook. found it in the field where her house was. last page just says 'if you're reading this... i lost.'")
    $ show_notebook_icon = True

    jump version_07
