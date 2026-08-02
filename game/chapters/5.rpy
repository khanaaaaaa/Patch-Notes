label version_05:

    narrator "\[ VERSION 0.5 - Feature Cut \]"
    pause 0.5

    narrator "Mina starts glitching. That's the only word for it."

    narrator "Mid-sentence, she just stops. Eyes open, breathing, but not there."
    narrator "Then she continues like nothing happened."

    show minaneutraltalk at center_char
    mina "I was thinking we could go to the river later and-"
    hide minaneutraltalk
    show minaneutralquiet at center_char
    narrator "She stops."
    narrator "Three seconds."
    hide minaneutralquiet
    show minasmiletalk at center_char
    mina "-and maybe some bread."
    hide minasmiletalk
    show minaneutralquiet at center_char
    narrator "You don't mention it. She doesn't know it happened."
    narrator "Then one afternoon she says something impossible."

    hide minaneutralquiet
    show minasmiletalk at center_char
    mina "Promise me something."
    hide minasmiletalk
    show minaneutralquiet at center_char
    eli "What?"
    hide minaneutralquiet
    show minasmiletalk at center_char
    mina "Promise me.."
    hide minasmiletalk
    show minaneutralquiet at center_char
    narrator "She stops.. longer this time.. her hands go still."
    hide minaneutralquiet
    show minasmiletalk at center_char
    mina "If I disappear..."
    hide minasmiletalk
    show minaneutralquiet at center_char
    narrator "She looks at her hands like she doesn't recognize them."
    hide minaneutralquiet
    show minaneutraltalk at center_char
    mina "...don't let them optimize you."
    hide minaneutraltalk
    show minaneutralquiet at center_char
    narrator "Then she blinks."
    hide minaneutralquiet
    show minaneutraltalk at center_char
    mina "Sorry, what was I saying?"
    hide minaneutraltalk
    show minaneutralquiet at center_char
    eli "You were talking about the river."
    hide minaneutralquiet
    show minaneutraltalk at center_char
    mina "Right, the river. Do you want to go?"
    hide minaneutraltalk
    show minaneutralquiet at center_char

    menu:
        "Go to the river.. don't mention it.":
            narrator "You go to the river."
            narrator "You skip stones."
            narrator "She laughs when yours goes further than hers."
            narrator "You memorize the sound."
            $ mina_trust += 1
        "\"Mina.. you said something about disappearing\"":
            $ eli_awareness += 1
            eli "Mina.. you said something about disappearing."
            hide minaneutralquiet
            show minaneutraltalk at center_char
            mina "I don't know what you mean."
            hide minaneutraltalk
            show minaneutralquiet at center_char
            eli "You said 'if I disappear, don't let them optimize you.'"
            hide minaneutralquiet
            show minaneutraltalk at center_char
            mina "That doesn't make any sense."
            hide minaneutraltalk
            show minaneutralquiet at center_char
            narrator "She laughs. It sounds right."
            narrator "But her eyes are going somewhere she can't tell you about."

    narrator "That night she knocks on your door. Late. Looks like she hasn't slept."

    hide minaneutralquiet
    show minaneutraltalk at center_char
    mina "I need to tell you something."
    mina "And I need you to not ask me how I know."
    hide minaneutraltalk
    show minaneutralquiet at center_char
    eli "Okay."
    hide minaneutralquiet
    show minaneutraltalk at center_char
    mina "I remember the previous versions."
    hide minaneutraltalk
    show minaneutralquiet at center_char
    eli "..What?"
    hide minaneutralquiet
    show minaneutraltalk at center_char
    mina "The river wasn't always there, and the mayor had a wife."
    hide minaneutraltalk
    show minaneutralquiet at center_char
    eli "How do you-"
    hide minaneutralquiet
    show minaneutraltalk at center_char
    mina "I've been pretending not to remember because I thought it was safer."
    mina "But they're removing people one by one, Eli."
    mina "And I think I'm next."
    hide minaneutraltalk
    show minaneutralquiet at center_char

    if mina_trust >= 2:
        eli "I know.. I've been keeping a notebook."
        hide minaneutralquiet
        show minaneutraltalk at center_char
        mina "Show me."
        hide minaneutraltalk
        show minaneutralquiet at center_char
        narrator "You show her. She reads every entry. Her face doesn't change but her hands grip the pages tighter."
        hide minaneutralquiet
        show minaneutraltalk at center_char
        mina "You remembered Petra."
        hide minaneutraltalk
        show minaneutralquiet at center_char
        eli "Of course, I did."
        hide minaneutralquiet
        show minaneutraltalk at center_char
        mina "Nobody else does."
        hide minaneutraltalk
        show minaneutralquiet at center_char
        narrator "She closes the notebook carefully. Like it was something fragile."
        hide minaneutralquiet
        show minaneutraltalk at center_char
    else:
        eli "Why are you telling me this now?"
        hide minaneutralquiet
        show minaneutraltalk at center_char
        mina "Because I found something."
        mina "And I might not get another chance."

    mina "Past the invisible walls past the edge of the world."
    mina "There's a white empty room."
    mina "Debug menus."
    mina "And a door."
    mina "It's locked."
    hide minaneutraltalk

    $ notebook_entries.append("Mina remembers everything. She found the ROOT door past the invisible walls.")
    $ chose_to_remember = True
    $ show_notebook_icon = True

    jump version_06
