import string
import random

SPACE_PROB = 0.18

def get_letter():
    global SPACE_PROB
    if random.random() < SPACE_PROB:
        return " "
    return random.choice(string.ascii_lowercase)

words = "".join(get_letter() for _ in range(1000000))
print words
