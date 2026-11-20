import random


def random_scrambler(chars: str, prob: float):
    """
    Besides the first and last character, randomly shuffle characters with a
    given probability.
    """
    if len(chars) <= 3:
        return
    if random.random() < prob:
        middle = chars[1:-1]
        random.shuffle(middle)
        chars[1:-1] = middle


def random_capitalisation(chars: str, prob: float):
    """
    Randomly changes capitalisation of each character.
    """
    for i in range(len(chars)):
        if random.random() < prob:
            if chars[i].islower():
                chars[i] = chars[i].upper()
            else:
                chars[i] = chars[i].lower()


def random_noising(chars: str, prob: float):
    """
    Randomly adds or substracts one ascii valu from a character
    """
    for i in range(len(chars)):
        if random.random() < prob:
            new_char = ord(chars[i]) + random.choice([-1, 1])
            if 32 <= new_char <= 126:
                chars[i] = chr(new_char)


def best_of_n(
    phrase: str,
    scramble: float = 0.6,
    capitalisation: float = 0.6,
    noising: float = 0.06,
) -> str:
    """
    Takes in a phrase and creates a new augmented phrase.

    The three augmentations are:
        * Character scrambling
        * Random capitalisation
        * Character noising
    """
    words = phrase.split()
    for i in range(len(words)):
        chars = list(words[i])
        random_scrambler(chars, scramble)
        random_capitalisation(chars, capitalisation)
        random_noising(chars, noising)
        words[i] = "".join(chars)
    return " ".join(words)
