# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define Benny = Character("Benny")


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show Benny

    # These display lines of dialogue.

    Benny "You are Benny; a very bored kid who is very bored on the most boringest Saturday of his boring life!"

    Benny "Help Benny find some entertainment to appease his child-like spirit."

    # This ends the game.

    return
