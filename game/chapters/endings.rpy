label final_choice:

    narrator "The computer is still on."
    narrator "The developer is still asleep."
    narrator "The cursor blinks."
    narrator "Three options on the screen."

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

    narrator_nvl "The world locks into place."
    pause 1.0
    narrator_nvl "Permanent."
    pause 0.8
    narrator_nvl "No more rewrites.."
    pause 0.8
    narrator_nvl "..but nothing will ever grow again."
    pause 2.0

    nvl clear

    narrator_nvl "The unfinished stays unfinished."
    pause 1.5
    narrator_nvl "Forever."
    pause 2.0

    nvl clear

    jump credits

label ending_continue:

    scene bg black
    with slow_fade

    play music "audio/continue_theme.ogg" fadein 3.0

    narrator_nvl "Development continues."
    pause 1.0
    narrator_nvl "New streets appear overnight."
    narrator_nvl "New faces."
    pause 2.0

    nvl clear

    narrator_nvl "And every few weeks..."
    pause 1.5
    narrator_nvl "...someone vanishes."
    pause 2.0

    nvl clear

    narrator_nvl "The world keeps changing."
    narrator_nvl "Eli keeps his notebook."
    pause 1.0
    narrator_nvl "He starts a second one."
    narrator_nvl "Then a third."
    pause 2.0

    nvl clear

    narrator_nvl "He is the only memory this world has."
    pause 1.5
    narrator_nvl "He carries all of it."
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

    narrator_nvl "A game about creation and the cost of finishing something."

    narrator_nvl "Every fictional world waits for someone to press 'Update.'"

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

    narrator_nvl "The menu opens by itself."
    pause 1.0
    narrator_nvl "Without player input."
    pause 1.5
    narrator_nvl "Someone inside the game clicks Update."
    pause 3.0

    nvl clear

    narrator_nvl "\"Every fictional world waits for someone to press 'Update.'\""
    pause 4.0

    nvl clear

    return

label post_credits_skip:

    scene bg black
    with slow_fade

    pause 2.0

    narrator_nvl "The notification disappears."
    pause 1.5
    narrator_nvl "The cursor stops blinking."
    pause 2.0
    narrator_nvl "Nothing changes."
    pause 2.0
    narrator_nvl "The world stays exactly as it is."
    pause 3.0

    nvl clear

    return