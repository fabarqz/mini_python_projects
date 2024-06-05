import random


class Labyrinth:
    def __init__(self, stages):
        self.stages = stages
        self.player_alive = True
        self.labyrinth_solution = self.generate_labyrinth()

    def generate_labyrinth(self):
        chambers = ["left", "middle", "right"]
        labyrinth_solution = [random.choice(chambers) for x in range(self.stages)]
        return labyrinth_solution

    def get_choice(self, solution):
        print(self.labyrinth_solution)
        try:
            if solution in ("left", "right"):
                chamber = (
                    input(
                        "The path before you splits into two, will you take the left or right path?"
                    )
                    .strip()
                    .lower()
                )
                if chamber not in ["left", "right", "Left", "Right"]:
                    raise ValueError(
                        "Invalid input. You can only pick between left and right"
                    )
            elif solution == "middle":
                chamber = (
                    input(
                        "The path before you splits into three, will you take the left,middle or right path?"
                    )
                    .strip()
                    .lower()
                )
                if chamber not in [
                    "left",
                    "right",
                    "Left",
                    "Right",
                    "middle",
                    "Middle",
                ]:
                    raise ValueError(
                        "Invalid input. You can only pick either left ,middle or right"
                    )
            return chamber
        except ValueError as e:
            print(e)

    def labyrinth_loop(self):
        current_labyrinth = self.labyrinth_solution
        for level in current_labyrinth:
            if not self.player_alive:
                break
            chosen_chamber = self.get_choice(level)
            if chosen_chamber == level:
                print("You picked the correct path so you can proceed further")
            else:
                print("You died")
                self.player_alive = False
                break


if __name__ == "__main__":
    get_stages = int(input("How many stages will the maze have? "))
    labrynth = Labyrinth(get_stages)
    labrynth.labyrinth_loop()
    # maze_one = labrynth.generate_labyrinth()

    # print(maze_one)
