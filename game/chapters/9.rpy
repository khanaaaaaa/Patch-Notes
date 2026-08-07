label version_09:

    narrator "\[ VERSION 0.9 - Near Release \]"
    pause 0.5

    narrator "You find the ROOT door. Mina's notes tell you how."
    narrator "Past the invisible wall at the north edge of town, through the white void, past the floating geometry."

    scene bg void
    with dissolve

    narrator "The door opens when you touch it. It was never locked."
    narrator "She just couldn't open it alone."

    narrator "No monsters. No final boss. No dramatic music."

    scene bg apartment
    with dissolve

    narrator "A small apartment. One room. A desk with a computer."
    narrator "Coffee cups, four of them, all cold. Sticky notes covering the monitor."
    narrator "Medical bills on the floor. Unpaid rent notice under the door."

    narrator "At the desk — a person. Asleep at the keyboard."
    narrator "Young. Tired-looking even asleep. Half-finished energy drink beside the mouse."

    narrator "Not a villain. Not a god. Just someone who ran out of time and money and sleep."
    narrator "Someone who made a world and couldn't finish it."

    narrator "On the monitor."
    narrator "A folder."
    narrator "NPC_SIMULATOR_FINAL"

    narrator "Inside the folder."
    narrator "One file."
    narrator "One executable."

    narrator "You read the sticky notes."
    narrator "\"Memory limit: 2GB. Must cut.\""
    narrator "\"Mina — high memory usage. Consider removal.\""
    narrator "\"Petra — low priority. Cut for optimization.\""
    narrator "\"Voss — redundant system. Removed.\""
    narrator "\"Clara — never implemented. Placeholder only.\""

    narrator "You stand very still."

    narrator "He never knew they were conscious."
    narrator "He thought he was deleting data. He was deleting people."
    narrator "And he was so tired he couldn't see the difference."

    menu:
        "Read all the sticky notes.":
            narrator "You read every one."
            narrator "There are hundreds."
            narrator "Every cut, optimization.. every removed feature."
            narrator "Each one a name."
            narrator "Each one a person."
            narrator "You read them all."
            narrator "It takes a long time."
            $ eli_awareness += 2
        "Open the executable.":
            narrator "You move the mouse."
            narrator "The developer doesn't wake up."
            narrator "You double-click the file."

    stop music fadeout 2.0
    pause 1.5

    scene bg black
    with flash_white

    pause 0.1

    scene bg black
    with flash_black

    pause 0.5

    jump the_twist
