import random


class Coin:
    @staticmethod
    def singleToss() -> str:
        return random.choice(["Heads", "Tails"])
