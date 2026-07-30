label version_05:

    narrator "\[ VERSION 0.5 - Feature Cut \]"
    pause 0.5

    narrator "Mina starts glitching."
    narrator "That's the only word for it."

    narrator "She'll be mid-sentence and just.. stop."
    narrator "Eyes open.. breathing... but not there."
    narrator "Then she'll continue like nothing happened."
    narrator "Half a second.. a full second... sometimes longer."

    mina "I was thinking we could go to the river later and-"
    narrator "She stops."
    narrator "Three seconds."
    mina "-and maybe some bread."
    narrator "You don't mention it."
    narrator "She doesn't know it happened."
    narrator "Then one afternoon, she says something impossible."

    mina "Promise me something."
    eli "What?"
    mina "Promise me.."
    narrator "She stops.. longer this time.. her hands go still."
    mina "If I disappear..."
    narrator "She looks at her hands like she doesn't recognize them."
    mina "...don't let them optimize you."
    narrator "Silence."
    narrator "Then she blinks."
    mina "Sorry, what was I saying?"
    eli "You were talking about the river."
    mina "Right, the river. Do you want to go?"

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
            mina "I don't know what you mean."
            eli "You said 'if I disappear, don't let them optimize you.'"
            mina "That doesn't make any sense."
            narrator "She laughs.. it sounds right."
            narrator "But her eyes are doing that thing again."
            narrator "Going somewhere else."
            narrator "Somewhere she can't tell you about."

    narrator "That night, she knocks on your door."
    narrator "It's late, and she looks like she hasn't slept."

    mina "I need to tell you something."
    mina "And I need you to not ask me how I know."
    eli "Okay."
    mina "I remember the previous versions."
    narrator "Silence."
    eli "..What?"
    mina "The river wasn't always there, and the mayor had a wife."
    eli "How do you-"
    mina "I've been pretending not to remember because I thought it was safer."
    mina "But they're removing people one by one, Eli."
    mina "And I think I'm next."

    if mina_trust >= 2:
        eli "I know.. I've been keeping a notebook."
        mina "Show me."
        narrator "You show her."
        narrator "She reads every entry."
        narrator "Her face doesn't change but her hands grip the pages tighter."
        mina "You remembered Petra."
        eli "Of course, I did."
        mina "Nobody else does."
        narrator "She closes the notebook carefully."
        narrator "Like it was something fragile."
    else:
        eli "Why are you telling me this now?"
        mina "Because I found something."
        mina "And I might not get another chance."

    mina "Past the invisible walls past the edge of the world."
    mina "There's a white empty room."
    mina "Debug menus."
    mina "And a door."
    mina "It's locked."

    $ notebook_entries.append("Mina remembers everything. She found the ROOT door past the invisible walls.")
    $ chose_to_remember = True
    $ show_notebook_icon = True

    jump version_06
