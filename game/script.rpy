# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

image waluigi = "images/Waluigi.png"
define w = Character("Waluigi")


# The game starts here.

label start:

    play music "audio/Wa-Elegy.mp3"

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show waluigi

    # These display lines of dialogue.

    w "Ah shit here we go again"

    w "Yet another attempt at making a dumb visual novel"

    w "I hope it works out this time"

    # This ends the game.

    return
