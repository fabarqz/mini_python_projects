import random


def passwordGenerator():
    lower = [
        "a",
        "b",
        "c",
        "d",
        "e",
        "f",
        "g",
        "h",
        "i",
        "j",
        "k",
        "l",
        "m",
        "n",
        "o",
        "p",
        "q",
        "r",
        "s",
        "t",
        "u",
        "v",
        "w",
        "x",
        "y",
        "z",
    ]
    upper = [
        "A",
        "B",
        "C",
        "D",
        "E",
        "F",
        "G",
        "H",
        "I",
        "J",
        "K",
        "L",
        "M",
        "N",
        "O",
        "P",
        "Q",
        "R",
        "S",
        "T",
        "U",
        "V",
        "W",
        "X",
        "Y",
        "Z",
    ]
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
    symbols = ["!", "@", "#", "$", "%", "*"]

    sampled_password = (
        random.sample(upper, 2)
        + random.sample(lower, 2)
        + random.sample(numbers, 2)
        + random.sample(symbols, 2)
    )

    random.shuffle(sampled_password)

    return sampled_password


x = passwordGenerator()

print("".join(str(a) for a in x))
