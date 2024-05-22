### Rock Paper Scissors ###

# This game without graphicals is so simple and with a AI random. You can try to make this game better

import time
import random
from enum import Enum

from colorama import Fore, init
init(autoreset=True)


class RockPaperScissors(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3


election = input(
    Fore.GREEN + "Select rock, papers, scissors: \n Rock = 1 \n Paper = 2 \n Scissors = 3 \n Election: "
)

if election not in ["1", "2", "3"]:
    print(Fore.RED + "Plis, select a corret number!")
    time.sleep(4)
else:
    election = int(election)

AI = random.randint(1, 3)

if (AI == 1 and election == 1) or (AI == 2 and election == 2) or (AI == 3 and election == 3):
    print(Fore.YELLOW + f"The AI use {AI}. It's a tie!")
    time.sleep(3)
elif (AI == 1 and election == 2) or (AI == 2 and election == 3) or (AI == 3 and election == 1):
    print(Fore.BLUE + f"The AI use {AI}. You win!")
    time.sleep(3)
elif (AI == 2 and election == 1) or (AI == 3 and election == 2) or (AI == 1 and election == 3):
    print(Fore.RED + f"The AI use {AI}. You lose!")
else:
    print(Fore.RED + "You no choose a correct name again. You lose!")
























easterEgg = "This is a easter egg only for developers that wants to add code and read it :) Thanks!"