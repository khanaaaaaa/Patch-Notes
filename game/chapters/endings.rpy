label final_choice:

    narrator "The cursor blinks. He's still asleep. Three options on the screen."
    narrator "You're the one who has to choose."

    menu:
        "Release - The world becomes permanent, everyone left unfinished stays unfinished forever.":
            jump ending_release
        "Continue Development - New content arrives, reality keeps changing.":
            jump ending_continue
        "Delete Project - Erase everything, no suffering.":
            jump ending_delete

label ending_release:

    scene bg black
    with slow_fade

    play music "audio/release_theme.ogg" fadein 3.0

    nvl clear

    narrator_nvl "The world stops changing."
    pause 1.0
    narrator_nvl "Everything that was left unfinished stays that way. Permanently."
    narrator_nvl "No more rewrites. No more additions. No more loss."
    pause 2.0

    nvl clear

    narrator_nvl "It's a kind of peace. The kind that comes from giving up on growth."
    pause 2.0

    nvl clear

    jump credits

label ending_continue:

    scene bg black
    with slow_fade

    play music "audio/continue_theme.ogg" fadein 3.0

    narrator_nvl "Development continues."
    pause 1.0
    narrator_nvl "New streets by morning. New faces who wave like they've always known you."
    pause 2.0

    nvl clear

    narrator_nvl "And every few weeks, quietly, someone is gone."
    pause 2.0

    nvl clear

    narrator_nvl "Eli fills notebook after notebook. He becomes the only continuous memory this world has."
    narrator_nvl "He carries everyone who was removed."
    narrator_nvl "It's a heavy thing to be the only one who remembers."
    pause 2.0

    nvl clear

    jump credits

label ending_delete:

    scene bg black
    with slow_fade

    stop music fadeout 2.0

    nvl clear

    narrator_nvl "..."
    pause 1.0
    narrator_nvl "..."
    pause 1.0
    narrator_nvl "..."
    pause 2.0

    nvl clear

    narrator_nvl "Nothing."
    pause 3.0

    jump credits

label credits:

    scene bg black
    with very_slow_fade

    nvl clear

    narrator_nvl "- PATCH NOTES -"
    pause 2.0

    nvl clear

    narrator_nvl "Every world someone builds is full of people they had to cut."
    narrator_nvl "Every finished thing is a graveyard of what it almost was."

    pause 2.0

    nvl clear

    stop music fadeout 4.0
    pause 4.0

    scene bg black
    with fade

    show screen fake_desktop
    pause 0.5

screen fake_desktop():
    zorder 200

    add Solid("#0e0e1a")

    text "NPC_SIMULATOR_FINAL" color "#1e1e2e" size 16 xpos 40 ypos 40

    text "recycle_bin.exe" color "#1e1e2e" size 14 xpos 40 ypos 900

    frame:
        xalign 0.98
        yalign 0.03
        background "#16162a"
        padding (24, 18)

        vbox:
            spacing 10

            text "Version 1.1 Available" color "#c8a2c8" size 24

            text "New content. Stability fixes.\nMemory optimizations." color "#6a5a6a" size 16

            null height 6

            textbutton "Update Now":
                xalign 0.5
                text_color "#f5c842"
                text_hover_color "#ffffff"
                text_size 20
                action [Hide("fake_desktop"), Jump("post_credits")]

            textbutton "Later":
                xalign 0.5
                text_color "#3a2a3a"
                text_hover_color "#5a4a5a"
                text_size 16
                action [Hide("fake_desktop"), Jump("post_credits_skip")]

label post_credits:

    scene bg black
    with flash_white

    pause 0.5

    scene bg black
    with fade

    pause 2.0

    nvl clear

    narrator_nvl "The menu opens on its own."
    pause 1.0
    narrator_nvl "No input. No one at the keyboard."
    pause 1.5
    narrator_nvl "Something inside the game pressed Update."
    pause 3.0

    nvl clear

    narrator_nvl "Every world someone builds is full of people they had to cut."
    pause 4.0

    nvl clear

    return

label post_credits_skip:

    scene bg black
    with slow_fade

    pause 2.0

    narrator_nvl "The notification closes."
    pause 1.5
    narrator_nvl "The cursor stops."
    pause 2.0
    narrator_nvl "The world stays exactly as it is."
    pause 2.0
    narrator_nvl "Which is, depending on how you look at it, either the saddest or the kindest outcome."
    pause 3.0

    nvl clear

    return