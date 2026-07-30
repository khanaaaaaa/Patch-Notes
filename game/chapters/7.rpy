label version_07:

    narrator "\[ VERSION 0.7 - Ambition \]"
    pause 0.5

    narrator "The developer decides the game needs more."
    narrator "More content, more systems, and more scope."
    narrator "You can feel it happening."

    narrator "Half the town wakes up with swords."
    narrator "Not metaphorically."
    narrator "Actual swords."
    narrator "The baker has one.. the mayor has one."
    narrator "The children have small ones."

    narrator "They talk about monsters."
    narrator "Creatures in the forest.. dungeons beneath the church."
    narrator "A great evil approaching from the East."

    eli "What's in the forest?"
    narrator "A villager grips his sword.. stares at the treeline."
    narrator "\"Something's coming. It just hasn't been added yet.\""

    narrator "Quest markers appear in the sky."
    narrator "Floating yellow diamonds pointing at empty fields."
    narrator "You follow one."
    narrator "It leads to a patch of grass."
    narrator "Nothing there."
    narrator "The marker pulses."
    narrator "Waiting."

    narrator "The other half of the town still acts like a cozy village."
    narrator "The flower seller's empty stall.. the library with no librarian."
    narrator "Children playing near the edge of the world."
    narrator "Two realities existing in the same space."
    narrator "Neither noticing the other."

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
