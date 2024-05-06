import random


class Dice:
    @staticmethod
    def getDiceType() -> int:
        AVAILABLE_DICE_TYPES = {4, 6, 8, 10, 12, 20}
        while True:
            try:
                dice_choice = int(input("What dice type would you like to roll: "))
                if dice_choice not in AVAILABLE_DICE_TYPES:
                    raise ValueError("Invalid dice type")

                return dice_choice
            except ValueError as e:
                print(f"Error. {e}. Try again")

    @staticmethod
    def roll(dice_type) -> int:
        result = random.randint(1, dice_type)
        return result


if __name__ == "__main__":
    dice_instance = Dice()
    current_dice = dice_instance.getDiceType()
    roll_result = dice_instance.roll(current_dice)
    print(roll_result)
