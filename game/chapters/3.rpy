label version_03:

    narrator "\[ VERSION 0.3 - Rewrites \]"
    pause 0.5
    narrator "It starts with something small enough to doubt."

    show minaneutralquiet at center_char
    eli "How's the painting?"
    hide minaneutralquiet
    show minaneutraltalk at center_char
    mina "The what?"
    hide minaneutraltalk
    show minaneutralquiet at center_char
    eli "The valley one. You've been working on it for months."
    hide minaneutralquiet
    show minasmiletalk at center_char
    mina "Eli, I don't paint."
    hide minasmiletalk
    show minaneutralquiet at center_char
    eli "Since when."
    hide minaneutralquiet
    show minasmiletalk at center_char
    mina "Since always. I actually find it kind of tedious, if I'm honest."
    hide minasmiletalk
    show minaneutralquiet at center_char
    narrator "She wrinkles her nose. You've seen that exact expression — standing at an easel, laughing at a mistake she'd made in the light."
    narrator "She'd asked you if the shadow looked right. You'd said yes. It hadn't."

    menu:
        "\"That's not funny.\"":
            eli "That's not funny."
            hide minaneutralquiet
            show minaneutraltalk at center_char
            mina "I'm not joking?"
            hide minaneutraltalk
            show minaneutralquiet at center_char
            narrator "She looks genuinely puzzled. That's almost worse."
            hide minaneutralquiet
        "\"I have a photo of you at an easel.\"":
            $ eli_awareness += 1
            eli "I have a photo. Of you. At an easel."
            narrator "You find it immediately, like part of you knew you'd need it."
            narrator "Mina at an easel, mid-laugh, paint on her sleeve."
            narrator "You hold the phone out."
            mina "..."
            narrator "She looks at it for a long time. Longer than she needs to."
            hide minaneutralquiet
            show minaneutraltalk at center_char
            mina "That isn't me."
            hide minaneutraltalk
            show minaneutralquiet at center_char
            narrator "She says it quietly. Not defensive. Almost careful."
            narrator "She hands the phone back. Her hands don't shake. Yours do."
            hide minaneutralquiet

    narrator "You visit the mayor. There's a wedding photo on his desk — him younger, a woman beside him, both squinting into sun."

    show mayorneutralquiet at center_char
    eli "Who's this?"
    hide mayorneutralquiet
    show mayorsmiletalk at center_char
    mayor "Hm? Oh, that came with the frame. Never got around to replacing it."
    hide mayorsmiletalk
    show mayorsmilequiet at center_char
    eli "That's you in the photo."
    hide mayorsmilequiet
    show mayorsmiletalk at center_char
    mayor "I've never been married. Wouldn't know what to do with myself."
    hide mayorsmiletalk
    show mayorneutralquiet at center_char
    narrator "He says it with the mild amusement of a man telling a story he's told before."
    narrator "You look at the photo again. The woman is gone. Just him, smiling at nothing."
    hide mayorneutralquiet

    narrator "That night you find a notebook in a kitchen drawer and start writing."
    narrator "You don't know what you're afraid of forgetting. You write it all anyway."
    narrator "In the morning, three pages are blank. The pen is still in your hand."

    $ notebook_entries.append("Mina - painting. valley scene, worked on it for months. she laughed when the light looked wrong. she KNOWS that painting.")
    $ notebook_entries.append("mayor's wife - was in the photo on his desk. then she wasn't. he didn't even blink.")
    $ notebook_entries.append("the river. it wasn't there. now it was always there. nobody thinks this is strange.")
    $ show_notebook_icon = True

    jump version_035
