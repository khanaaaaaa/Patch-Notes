label final_choice:

    narrator "The computer is still on."
    narrator "The developer is still asleep."
    narrator "The cursor blinks."
    narrator "Three options on the screen"

    menu:
        "Release - The world becomes permanent, everyone left unfinished stays unfinished forever.":
            jump ending_release
        "Continue Development - New content arrives, reality keeps changing.":
            jump ending_continue
        "Delete Project - Erase everything, no suffering.":
            jump ending_delete

label ending_release:

    scene bg black
    with fade

    narrator "The world locks into place."
    narrator "Permanent."
    narrator "No more rewrites.."
    narrator "..but nothing will ever grow again."
    narrator "The infinished stays unfinished."
    narrator "Forever."

    jump credits

label ending_continue:

    scene bg black
    with fade

    narrator "Development continues."
    narrator "New streets appear overnight."
    narrator "New faces."
    narrator "And every few weeks..."
    narrator "...someone vanishes."
    narrator "The world keeps changing."
    narrator "Eli keeps his notebook."
    narrator "He is the only memory this world has."

    jump credits

label ending_delete:

    scene bg black
    with fade

    narrator "..."
    narrator "..."
    narrator "Nothing."

    jump credits

label credits:

    scene bg black
    with fade

    narrator "- PATCH NOTES -"
    narrator "A game about creaton and the cost of finishing something."
    narrator " "
    narrator "Every fictional world waits for someone to press 'Update.'"

    pause 2.0

    narrator "..."
    narrator "A notification appears on the desktop."
    narrator " "
    narrator "[ Version 1.1 Available ]"
    narrator "The menu opens by itself."
    narrator "Without player input."
    narrator "Someone inside the game clicks Update."

    scene bg black
    with fade

    narrator "\"Every fictional world waits for someone to press 'Update.'\""

    return