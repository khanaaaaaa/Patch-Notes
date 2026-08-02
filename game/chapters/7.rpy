label version_07:

    narrator "\[ VERSION 0.7 - Ambition \]"
    pause 0.5
    narrator "You can feel it happening — more content, more systems, more scope."

    narrator "Half the town wakes up with swords. Not metaphorically. Actual swords."
    narrator "The baker has one. The mayor has one. The children have small ones."

    narrator "They talk about monsters. Creatures in the forest, dungeons beneath the church."
    narrator "A great evil approaching from the East."

    eli "What's in the forest?"
    narrator "A villager grips his sword.. stares at the treeline."
    narrator "\"Something's coming. It just hasn't been added yet.\""

    narrator "Quest markers appear in the sky — floating yellow diamonds pointing at empty fields."
    narrator "You follow one. Patch of grass. Nothing there. The marker pulses. Waiting."

    narrator "The other half still acts like a cozy village. The empty stall, the library with no librarian."
    narrator "Two realities in the same space. Neither noticing the other."

    menu:
        "Follow the quest markers.":
            narrator "You follow every marker."
            narrator "Every single one leads to nothing."
            narrator "The game is promising things it hasn't built yet."
            $ eli_awareness += 1
        "Go back to the field where Mina's house was.":
            narrator "You go back to the field."
            narrator "You sit with her notebook."
            narrator "You read it again."
            narrator "You read the parts she wrote about you."
            narrator "She wrote that you were the only one who made the loop feel different."
            narrator "You didn't know she noticed."
            $ mina_trust += 1

    jump version_08
