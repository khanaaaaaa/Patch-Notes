label version_03:

    narrator "\[ VERSION 0.3 - Rewrites \]"
    pause 0.5
    narrator "It starts small. The kind of thing you could explain away."

    show minaneutralquiet at center_char
    eli "Mina, how's the painting going?"
    hide minaneutralquiet
    show minaneutraltalk at center_char
    mina "What painting?"
    hide minaneutraltalk
    show minaneutralquiet at center_char
    eli "The one you've been working on for months.. the one of the valley?"
    hide minaneutralquiet
    show minasmiletalk at center_char
    mina "Eli, I don't paint."
    hide minasmiletalk
    show minaneutralquiet at center_char
    eli "..What?"
    hide minaneutralquiet
    show minasmiletalk at center_char
    mina "I've never painted, I actually kind of hate art."
    hide minasmiletalk
    show minaneutralquiet at center_char
    narrator "She wrinkles her nose in genuine distaste."
    narrator "You've seen that expression before — when she made a mistake on a canvas and laughed."
    narrator "When she showed you the valley painting and asked if the light looked right."

    menu:
        "\"You're joking.\"":
            eli "You're joking."
            hide minaneutralquiet
            show minaneutraltalk at center_char
            mina "Why would I joke about that?"
            hide minaneutraltalk
            show minaneutralquiet at center_char
            narrator "She genuinely looks confused."
            hide minaneutralquiet
        "\"I have a photo of you painting on my phone.\"":
            $ eli_awareness += 1
            eli "I have a photo of you painting on my phone."
            narrator "You check."
            narrator "The photo is there."
            narrator "Mina, standing at an easel, laughing at the camera."
            narrator "You show her."
            mina "..."
            narrator "She stares at it for a long time."
            hide minaneutralquiet
            show minaneutraltalk at center_char
            mina "That's not me."
            hide minaneutraltalk
            show minaneutralquiet at center_char
            narrator "She hands the phone back. Her hands are steady. Yours aren't."
            hide minaneutralquiet

    narrator "You visit the mayor. There's a photo on his desk — a wedding photo. He's younger, smiling, with a woman beside him."

    show mayorneutralquiet at center_char
    eli "Mayor Aldric, who is this?"
    hide mayorneutralquiet
    show mayorsmiletalk at center_char
    mayor "Hm? Oh, that's just a stock photo that came with the frame."
    hide mayorsmiletalk
    show mayorsmilequiet at center_char
    eli "That's you.. in the photo."
    hide mayorsmilequiet
    show mayorsmiletalk at center_char
    mayor "I've never been married, never had the time."
    hide mayorsmiletalk
    show mayorneutralquiet at center_char
    narrator "He says it without blinking."
    narrator "You look at the photo again. The woman is gone. Just him now, smiling alone."
    hide mayorneutralquiet

    narrator "That night you start a notebook. Everything you remember."
    narrator "Mina's painting. The mayor's wife. The river."
    narrator "You fall asleep with the pen in your hand. In the morning, three pages are blank."

    $ notebook_entries.append("Mina used to love painting especially scenary. She laughed especially when she made mistakes.")
    $ notebook_entries.append("Mayor Aldric had a wife, she was in the wedding photo. Then she suddenly wasn't.")
    $ notebook_entries.append("The river appeared overnight, and everyone acts like it was already there.")
    $ show_notebook_icon = True

    jump version_035
