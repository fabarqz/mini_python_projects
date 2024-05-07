import random


class Dice:
    @staticmethod
    def getDiceType() -> int:
        AVAILABLE_DICE_TYPES = {4, 6, 8, 10, 12, 20}
        while True:
            try:
                dice_choice = int(input("What dice type would you like to roll? "))
                if dice_choice not in AVAILABLE_DICE_TYPES:
                    raise ValueError("Invalid dice type")

                return dice_choice
            except ValueError as e:
                print(f"Error. {e}. Try again")

    @staticmethod
    def getPair() -> list[int]:

        inputList = [
            int(item)
            for item in input(
                "Enter the dice type you wish to roll followed by the number of rolls separated by a space: "
            ).split()
        ]
        dice_type = inputList[0]
        number_rolls = inputList[1]

        result_list = Dice.multiple_rolls(dice_type, number_rolls)

        return result_list

    @staticmethod
    def getRolls() -> int:
        number_rolls = int(input("How many times would you like to roll the dice? "))
        return number_rolls

    @staticmethod
    def multiple_rolls(dice_choice, number_rolls) -> list:
        results = []

        for i in range(number_rolls):
            roll_result = Dice.roll(dice_choice)
            results.append(roll_result)

        return results

    @staticmethod
    def roll(dice_type) -> int:
        result = random.randint(1, dice_type)
        return result


if __name__ == "__main__":
    dice_instance = Dice()
    # current_dice = dice_instance.getDiceType()
    # number_rolls = dice_instance.getRolls()
    # results = dice_instance.multiple_rolls(current_dice, number_rolls)
    # roll_result = dice_instance.roll(current_dice)

    dice_results = dice_instance.getPair()

    print(dice_results)
