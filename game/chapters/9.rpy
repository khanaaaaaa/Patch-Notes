label version_09:

    narrator "\[ VERSION 0.9 - Near Release \]"
    pause 0.5

    narrator "You find the ROOT door."
    narrator "Mina's notes tell you how."
    narrator "Past the invisible wall at the north edge of town."
    narrator "Through the white void."
    narrator "Past the floating geometry and the error logs."

    scene bg black
    with dissolve

    narrator "The door is exactly where she said it would be."
    narrator "It opens when you touch it."
    narrator "It was never locked."
    narrator "She just couldn't open it alone."

    narrator "Inside."
    narrator "No monsters."
    narrator "No final boss."
    narrator "No dramatic music."

    narrator "A small apartment."
    narrator "One room."
    narrator "A desk with a computer."
    narrator "Coffee cups, four of them.. all cold."
    narrator "Sticky notes covering the monitor."
    narrator "Medical bills on the floor."
    narrator "Unpaid rent notice under the door."

    narrator "And at the desk."
    narrator "A person."
    narrator "Asleep at the keyboard."
    narrator "Young, and tired-looking even asleep."
    narrator "A half-finished energy drink beside the mouse."

    narrator "This is not a villain, or god."
    narrator "Just someone who ran out of time and money.. and sleep."
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

    narrator "He never knew."
    narrator "He never knew they were conscious."
    narrator "He thought he was deleting data."
    narrator "He was deleting people."

    narrator "And he was so tired."
    narrator "So tired.. he couldn't see the difference."

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

    jump the_twist
