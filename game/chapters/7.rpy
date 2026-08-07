label version_07:

    narrator "\[ VERSION 0.7 - Ambition \]"
    pause 0.5
    narrator "You can feel the developer wanting more. The world strains at the seams of what it was."

    narrator "Half the town wakes up with swords. Not ceremonial. Not decorative. Actual swords, worn like they've always had them."
    narrator "The baker's is propped against the bread rack. The mayor's is on his desk where the wedding photo used to be."
    narrator "The children have small ones. They seem pleased about this."

    narrator "Everyone talks about a darkness coming from the East."
    narrator "Creatures in the forest. Dungeons under the church."

    eli "What's in the forest?"
    narrator "A man you don't recognise grips his sword and stares at the treeline."
    narrator "\"Something. It just hasn't arrived yet.\""

    narrator "Yellow quest markers hang in the sky like punctuation for a sentence nobody wrote."
    narrator "You follow one to a field. Stand there. The marker pulses above you, patient."
    narrator "There is nothing here. There has never been anything here. The game is making promises it hasn't kept yet."

    narrator "The other half of town hasn't changed. The empty flower stall. The library with its dented cushion."
    narrator "Two versions of the same place, occupying the same coordinates, neither aware of the other."

    scene bg library
    with dissolve

    menu:
        "Follow the quest markers.":
            scene bg town
            with dissolve
            narrator "You follow every single one."
            narrator "Fields. Empty lots. A cave entrance with nothing inside."
            narrator "The game is a list of intentions."
            $ eli_awareness += 1
        "Go back to the field.":
            scene bg field
            with dissolve
            narrator "You sit with her notebook again."
            narrator "You find the pages she wrote about you near the back."
            narrator "She wrote that you were the only one who ever seemed to notice the loop."
            narrator "That it made the days feel different, even when they weren't."
            narrator "You didn't know she'd been watching."
            $ mina_trust += 1

    jump version_08
