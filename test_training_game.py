#! python3
from soundrts import config
from soundrts.mapfile import Map

config.mods = ""

from soundrts import clientmain


if __name__ == "__main__":
    clientmain.init_media()
#    clientmain.TrainingGame(Map("multi/jl5.txt"), ["test", "easy"], ["random_faction", "random_faction"]).run(speed=20)
    clientmain.TrainingGame(Map("multi/jl5.txt"),
                            ["test", "aggressive", "easy"],
                            ["random_faction", "random_faction", "random_faction"],
                            ["1", "1", "2"]
                            ).run(speed=20)
