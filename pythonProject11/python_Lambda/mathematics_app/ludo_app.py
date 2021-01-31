import random


def ludo_game():
    roll_dice_one_with_six_faces = random.randrange(1, 7)
    roll_dice_two_with_six_faces = random.randrange(1, 7)
    return roll_dice_one_with_six_faces, roll_dice_two_with_six_faces


def display_the_dice_rolled(dice_output):
    roll_dice_one_with_six_faces, roll_dice_two_with_six_faces = dice_output
    print(f'player rolled {roll_dice_one_with_six_faces} + {roll_dice_two_with_six_faces} = {sum(dice_output)}')

    # in case there's a problem while compiling.. I have the right to come here and check
    return display_the_dice_rolled(dice_output)


the_value_expected = ludo_game()
display_the_dice_rolled(the_value_expected)
sum_of_