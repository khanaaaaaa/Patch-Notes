label version_035:

    narrator "[ VERSION 0.35 - Broken Build ]"
    pause 0.5

    scene bg black

    narrator "Something breaks."
    narrator "Not metaphorically."
    narrator "Something in the world itself breaks."

    narrator "It rains inside the bakery."
    narrator "Not through the ceiling."
    narrator "Just... inside."
    narrator "Falling from nothing."
    narrator "The bread gets wet."
    narrator "You stand in indoor rain and don't know what to do."

    narrator "A tree outside your window is floating."
    narrator "Three feet off the ground."
    narrator "Rotating slowly."
    narrator "Nobody mentions it."

    narrator "You see the flower seller walk through a wall."
    narrator "She comes out the other side still talking about her roses."

    narrator "Time skips."
    narrator "You are eating breakfast."
    narrator "Then you are watching the sunset."
    narrator "You don't remember the hours between."

    narrator "One morning, the sun doesn't rise."
    narrator "It stays dark."
    narrator "People go about their day like normal."
    narrator "Mina visits."

    show minaneutraltalk at center_char
    mina "Good morning!"
    hide minaneutraltalk
    show minaneutralquiet at center_char
    eli "Mina... the sun hasn't risen."
    hide minaneutralquiet
    show minasmiletalk at center_char
    mina "It's a beautiful day, isn't it?"
    hide minasmiletalk
    show minaneutralquiet at center_char
    eli "It's pitch black outside."
    hide minaneutralquiet
    show minasmiletalk at center char
    mina "Perfect baking weather."
    hide minasmiletalk
    show minaneutralquiet at center_char
    narrator "She smiles."
    narrator "You look at her for a long time."

    menu:
        "\"Are you okay?\"":
            eli "Are you okay?"
            hide minaneutralquiet
            show minasmiletalk at center_char
            mina "I'm always okay."
            hide minasmiletalk
            show minaneutralquiet at center_char
            narrator "She says it like a fact."
            narrator "Like something she was told to say."
            hide minaneutralquiet
            $ mina_trust += 1
        "\"Do you notice anything wrong with the sky?\"":
            eli "Do you notice anything wrong with the sky?"
            mina "..."
            narrator "She pauses."
            narrator "Just for a second."
            narrator "Her eyes go somewhere else."
            hide minaneutralquiet
            show minaneutraltalk at center_char
            mina "The sky looks fine to me."
            hide minaneutraltalk
            show minaneutralquiet at center_char
            narrator "But her voice is quieter than usual."
            hide minaneutralquiet
            $ mina_trust += 2

    jump version_04

label version_04:

    narrator "[ VERSION 0.4 - Optimization ]"
    pause 0.5

    narrator "The flower seller disappeared on a Tuesday."
    narrator "You notice because you bought roses from her every week."
    narrator "For no reason. Just because they were there."

    show minaneutralquiet at center_char
    eli "Where's the flower seller?"
    hide minaneutralquiet
    show minaneutraltalk at center_char
    mina "The flowers are self-service.. they always have been."
    hide minaneutraltalk
    show minaneutralquiet at center_char
    eli "She had a name, it was Petra."
    hide minaneutralquiet
    show minaneutraltalk at center_char
    mina "Who?"
    hide minaneutraltalk
    show minaneutralquiet at center_char
    eli "Petra, red hair. She always gave me an extra stem."
    hide minaneutralquiet
    show minaneutraltalk at center_char
    mina "Eli, there's no one by that name in Maple Crossing."
    hide minaneutraltalk

    narrator "You check your notebook."
    narrator "There is a page that says PETRA - red hair - extra stem - Tuesday roses."
    narrator "The ink is faded."
    narrator "Getting fainter as you watch."

    narrator "The librarian disappears on a Thursday."
    narrator "His name was Mr. Voss."
    narrator "He recommended books. He remembered what you liked."
    narrator "He had a cat that slept on the returns desk."

    show mayorsmilequiet at center_char
    eli "What happened to Mr. Voss?"
    hide mayorsmilequiet
    show mayorsmiletalk at center_char
    mayor "The library has always been self-service, son."
    hide mayorsmiletalk
    show mayorsmilequiet at center_char
    eli "He had a cat."
    hide mayorsmilequiet
    show mayorsmiletalk at center_char
    mayor "Libraries don't allow animals."
    hide mayorsmiletalk 
    narrator "The cat is gone too."
    narrator "There is a dent in the cushion on the returns desk."
    narrator "The shape of something small that used to sleep there."

    narrator "You start hearing it at night."
    narrator "Not a voice exactly."
    narrator "More like a system sound."
    narrator "Low. Flat. Final."
    narrator "\"Optimization complete.\""
    narrator "\"Optimization complete.\""
    narrator "\"Optimization complete.\""

    $ notebook_entries.append("Petra the flower seller. Removed Tuesday. Red hair. Extra stem.")
    $ notebook_entries.append("Mr. Voss the librarian. Removed Thursday. Had a cat. Cat also gone.")
    $ show_notebook_icon = True

    jump version_05
