label version_035:

    narrator "\[ VERSION 0.35 - Broken Build \]"
    pause 0.5

    scene bg black

    narrator "Something in the world breaks. Not a metaphor."

    narrator "It rains inside the bakery. Not through the ceiling — just inside, from nothing, falling straight down."
    narrator "The bread gets wet. You stand in it for a while, unsure what the correct response is."

    narrator "A tree outside your window is rotating slowly, three feet off the ground."
    narrator "The woman next door walks past it without looking up."

    narrator "The flower seller walks through a wall. Comes out the other side mid-sentence about her roses."

    narrator "You eat breakfast. Then it's evening. The hours between are just — gone."

    narrator "One morning the sun doesn't come up. The town goes about its business in the dark."
    narrator "Mina arrives at the usual time."

    show minaneutraltalk at center_char
    mina "Morning!"
    hide minaneutraltalk
    show minaneutralquiet at center_char
    eli "Mina. The sun."
    hide minaneutralquiet
    show minasmiletalk at center_char
    mina "Lovely day, isn't it."
    hide minasmiletalk
    show minaneutralquiet at center_char
    eli "It's completely dark outside."
    hide minaneutralquiet
    show minasmiletalk at center_char
    mina "Good light for baking."
    hide minasmiletalk
    show minaneutralquiet at center_char
    narrator "She smiles. You study her face the way you'd study a word you suddenly can't spell."

    menu:
        "\"Are you alright?\"":
            eli "Are you alright?"
            hide minaneutralquiet
            show minasmiletalk at center_char
            mina "I'm always alright."
            hide minasmiletalk
            show minaneutralquiet at center_char
            narrator "Five words. No hesitation. Like a door with a lock on the inside."
            hide minaneutralquiet
            $ mina_trust += 1
        "\"Look at the sky and tell me what you see.\"":
            eli "Look at the sky. Tell me what you see."
            mina "..."
            narrator "She goes still. Not frozen — just very, very quiet."
            hide minaneutralquiet
            show minaneutraltalk at center_char
            mina "Looks fine to me."
            hide minaneutraltalk
            show minaneutralquiet at center_char
            narrator "Her voice drops half a register. She doesn't look at the sky."
            hide minaneutralquiet
            $ mina_trust += 2

    jump version_04

label version_04:

    narrator "\[ VERSION 0.4 - Optimization \]"
    pause 0.5

    narrator "Petra disappears on a Tuesday. You only notice because you'd bought roses from her every week — not for anyone, just because she was there."

    show minaneutralquiet at center_char
    eli "Where's the flower stall?"
    hide minaneutralquiet
    show minaneutraltalk at center_char
    mina "It's self-service. Always has been."
    hide minaneutraltalk
    show minaneutralquiet at center_char
    eli "There was a woman. Petra. Red hair."
    hide minaneutralquiet
    show minaneutraltalk at center_char
    mina "I don't know anyone by that name."
    hide minaneutraltalk
    show minaneutralquiet at center_char
    eli "She always gave me an extra stem."
    hide minaneutralquiet
    show minaneutraltalk at center_char
    mina "Eli."
    hide minaneutraltalk
    show minaneutralquiet at center_char
    narrator "She says your name the way people do when they're deciding whether to be gentle."
    hide minaneutralquiet

    narrator "You open your notebook. PETRA - red hair - extra stem - Tuesdays. The ink is fading as you read it."

    narrator "Mr. Voss goes on a Thursday. He ran the library. Remembered what you liked, recommended things you didn't ask for, had a grey cat that slept on the returns desk."

    scene bg library
    with dissolve

    show mayorsmilequiet at center_char
    eli "What happened to the librarian?"
    hide mayorsmilequiet
    show mayorsmiletalk at center_char
    mayor "Always been self-service, son. Better that way, if you ask me."
    hide mayorsmiletalk
    show mayorsmilequiet at center_char
    eli "He had a cat."
    hide mayorsmilequiet
    show mayorsmiletalk at center_char
    mayor "Libraries don't allow animals. Health code."
    hide mayorsmiletalk
    narrator "The cat's cushion is still on the returns desk. There's a dent in it the exact shape of something that used to sleep there."

    scene bg town
    with dissolve

    narrator "That night you hear it. Not a voice. More like a notification sound, if notification sounds had weight."
    narrator "\"Optimization complete.\""
    narrator "\"Optimization complete.\""
    narrator "\"Optimization complete.\""

    $ notebook_entries.append("Petra. flower stall. red hair, always gave me an extra stem on tuesdays. gone tuesday. nobody remembers her name.")
    $ notebook_entries.append("mr voss - library. had a cat, grey, slept on the returns desk. both gone thursday. there's still a dent in the cushion.")
    $ show_notebook_icon = True

    jump version_05
