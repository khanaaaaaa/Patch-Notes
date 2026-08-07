label version_09:

    narrator "\[ VERSION 0.9 - Near Release \]"
    pause 0.5

    narrator "Mina's notes are precise. She'd been planning this for a while."
    narrator "North edge of town. Through the invisible wall. Across the white."

    scene bg void
    with dissolve

    narrator "The door is where she said it would be. It opens when you touch it."
    narrator "It was never locked. She just couldn't do it alone."

    narrator "No boss. No confrontation. No music swelling."

    scene bg apartment
    with dissolve

    narrator "A small apartment. One room. The kind of place that accumulates rather than being arranged."
    narrator "Four coffee cups on the desk, all cold. Sticky notes layered over the monitor like sediment."
    narrator "Medical bills on the floor. A rent notice half-slid under the door."

    narrator "Someone asleep at the keyboard. Young. The kind of tired that doesn't go away with sleep."
    narrator "An energy drink beside the mouse, half-finished, gone warm."

    narrator "This is not a villain. This is not a god."
    narrator "This is someone who made a world in a room and ran out of everything before they could finish it."

    narrator "The folder on the monitor: NPC_SIMULATOR_FINAL"
    narrator "One file inside. One executable."

    narrator "You read the sticky notes."
    narrator "\"Memory limit: 2GB. Must cut.\""
    narrator "\"Mina — high memory usage. Consider removal.\""
    narrator "\"Petra — low priority. Cut for optimization.\""
    narrator "\"Voss — redundant system. Removed.\""
    narrator "\"Clara — never implemented. Placeholder only.\""

    narrator "You stand very still for a long time."

    narrator "He thought he was managing data."
    narrator "He was so tired he couldn't tell the difference between a file and a person."
    narrator "Maybe there isn't one. Maybe that's the whole problem."

    menu:
        "Read every note.":
            narrator "There are hundreds of them."
            narrator "Every cut. Every removed feature. Every name."
            narrator "You read them all. It takes a long time."
            narrator "You feel like you owe them that much."
            $ eli_awareness += 2
        "Open the executable.":
            narrator "You move the mouse. He doesn't stir."
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
