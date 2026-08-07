label version_02:

    narrator "\[ VERSION 0.2 - Expansion \]"
    narrator "The wrongness isn't loud. It's the kind you feel in your teeth."

    scene bg town
    with dissolve

    narrator "There's a river. There are mountains. A church with a bell tower you've apparently heard your whole life."
    narrator "A man you've never seen waves at you like you owe him money in the best possible way."

    show minaneutralquiet at center_char
    eli "The river."
    hide minaneutralquiet
    show minasmiletalk at center_char
    mina "What about it?"
    hide minasmiletalk
    show minaneutralquiet at center_char
    eli "Was it always there?"
    hide minaneutralquiet
    show minasmiletalk at center_char
    mina "You used to skip stones there. You were terrible at it."
    hide minasmiletalk
    show minaneutralquiet at center_char
    narrator "She says it with the ease of someone recounting a real memory. The detail about being terrible is a nice touch."
    narrator "You don't remember any of it."

    menu:
        "\"Right. Yeah.\"":
            eli "Right. Yeah."
            narrator "You let it settle over you like a coat that doesn't quite fit."
            hide minaneutralquiet
        "\"Mina, there was no river yesterday.\"":
            $ eli_awareness += 1
            eli "There was no river yesterday."
            hide minaneutralquiet
            show minasmiletalk at center_char
            mina "Eli."
            hide minasmiletalk
            show minaneutralquiet at center_char
            eli "I'm not being strange. There was grass. Just grass."
            hide minaneutralquiet
            show minasmiletalk at center_char
            mina "You're tired. You work too much."
            hide minasmiletalk
            show minaneutralquiet at center_char
            narrator "She laughs. It's warm and familiar and lands exactly where a laugh should."
            narrator "Which is, somehow, the most unsettling part."
            hide minaneutralquiet

    narrator "Some of the new buildings are beautiful. Facades with real detail, window boxes, carved lintels."
    narrator "You try a door. Inside: nothing. White. Not a room — the absence of one."
    narrator "A staircase ends four feet off the ground. You stand beneath it for a while."

    narrator "Near the edge of town, children are playing some game with complicated rules."
    narrator "One of them stops when she notices where you're looking."

    show childtalk at center_char
    child "Don't go over there."
    hide childtalk
    show childquiet at center_char
    eli "Why?"
    hide childquiet
    show childtalk at center_char
    child "The world stops."
    hide childtalk
    show childquiet at center_char
    narrator "She says it the way you'd say the sky is blue. Factual. Slightly bored."
    hide childquiet
    show childtalk at center_char
    child "Everybody knows."
    hide childtalk
    show childquiet at center_char
    narrator "She goes back to her game."
    narrator "You stand at the place where the grass changes texture and doesn't cross."
    hide childquiet

    jump version_03