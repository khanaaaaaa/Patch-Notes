label version_05:

    narrator "\[ VERSION 0.5 - Feature Cut \]"
    pause 0.5

    narrator "Mina starts doing something she doesn't know she's doing."

    narrator "Mid-sentence, she stops. Eyes open, breathing, present in every physical sense."
    narrator "Then she picks up exactly where she left off, like a record that skipped."

    show minaneutraltalk at center_char
    mina "I was thinking we could go to the river later and-"
    hide minaneutraltalk
    show minaneutralquiet at center_char
    narrator "Three seconds. Maybe four."
    hide minaneutralquiet
    show minasmiletalk at center_char
    mina "-get some bread on the way back."
    hide minasmiletalk
    show minaneutralquiet at center_char
    narrator "You don't say anything. There's nothing to say that wouldn't sound like an accusation."
    narrator "Then one afternoon she looks at her hands mid-conversation and says:"

    hide minaneutralquiet
    show minasmiletalk at center_char
    mina "Promise me something."
    hide minasmiletalk
    show minaneutralquiet at center_char
    eli "Depends what it is."
    hide minaneutralquiet
    show minasmiletalk at center_char
    mina "Promise me first."
    hide minasmiletalk
    show minaneutralquiet at center_char
    narrator "She stops. Her hands go still in her lap."
    hide minaneutralquiet
    show minasmiletalk at center_char
    mina "If I disappear..."
    hide minasmiletalk
    show minaneutralquiet at center_char
    narrator "She's looking at her hands like she's never seen them before."
    hide minaneutralquiet
    show minaneutraltalk at center_char
    mina "...don't let them make you smaller."
    hide minaneutraltalk
    show minaneutralquiet at center_char
    narrator "Then she blinks. Comes back."
    hide minaneutralquiet
    show minaneutraltalk at center_char
    mina "Sorry — what was I saying?"
    hide minaneutraltalk
    show minaneutralquiet at center_char
    eli "The river."
    hide minaneutralquiet
    show minaneutraltalk at center_char
    mina "Right. Do you want to?"
    hide minaneutraltalk
    show minaneutralquiet at center_char

    menu:
        "Go. Don't bring it up.":
            narrator "You go. You skip stones. She wins, which she always does, and laughs about it in a way that sounds like her."
            narrator "You try to hold the sound of it somewhere it won't fade."
            $ mina_trust += 1
        "\"You said something about disappearing.\"":
            $ eli_awareness += 1
            eli "You said something. About disappearing."
            hide minaneutralquiet
            show minaneutraltalk at center_char
            mina "I don't think I did."
            hide minaneutraltalk
            show minaneutralquiet at center_char
            eli "'Don't let them make you smaller.' Those were your words."
            hide minaneutralquiet
            show minaneutraltalk at center_char
            mina "That doesn't sound like me."
            hide minaneutraltalk
            show minaneutralquiet at center_char
            narrator "She laughs a little. It almost lands."
            narrator "Her eyes are somewhere you can't follow."

    narrator "She comes to your door that night. Late enough that you'd already given up on the day."
    narrator "She looks like someone who's been awake deciding something."

    hide minaneutralquiet
    show minaneutraltalk at center_char
    mina "I need to tell you something and I need you to not ask me how I know it."
    hide minaneutraltalk
    show minaneutralquiet at center_char
    eli "Alright."
    hide minaneutralquiet
    show minaneutraltalk at center_char
    mina "I remember the other versions."
    hide minaneutraltalk
    show minaneutralquiet at center_char
    eli "The other—"
    hide minaneutralquiet
    show minaneutraltalk at center_char
    mina "The river wasn't always there. The mayor had a wife. I know because I was there when they weren't."
    hide minaneutraltalk
    show minaneutralquiet at center_char
    eli "How long have you—"
    hide minaneutralquiet
    show minaneutraltalk at center_char
    mina "A while. I thought if I stayed quiet it would be safer."
    mina "I don't think quiet is going to save me."
    hide minaneutraltalk
    show minaneutralquiet at center_char

    if mina_trust >= 2:
        eli "I've been writing things down. In case."
        hide minaneutralquiet
        show minaneutraltalk at center_char
        mina "Show me."
        hide minaneutraltalk
        show minaneutralquiet at center_char
        narrator "You show her. She reads slowly. Her expression doesn't change but at some point her grip on the pages tightens."
        hide minaneutralquiet
        show minaneutraltalk at center_char
        mina "You wrote about Petra."
        hide minaneutraltalk
        show minaneutralquiet at center_char
        eli "Of course."
        hide minaneutralquiet
        show minaneutraltalk at center_char
        mina "Nobody else does."
        hide minaneutraltalk
        show minaneutralquiet at center_char
        narrator "She closes the notebook like it's something that could break."
        hide minaneutralquiet
        show minaneutraltalk at center_char
    else:
        eli "Why tell me now?"
        hide minaneutralquiet
        show minaneutraltalk at center_char
        mina "Because I found something."
        mina "And I don't know how much time I have left to tell anyone."

    mina "Past the edge of the map there's a white room. Empty. Debug menus on the walls."
    mina "And a door."
    mina "I couldn't open it alone."
    hide minaneutraltalk

    $ notebook_entries.append("Mina remembers. all of it. she's been pretending not to. found something past the edge - white room, debug stuff, a door.")
    $ chose_to_remember = True
    $ show_notebook_icon = True

    jump version_06
