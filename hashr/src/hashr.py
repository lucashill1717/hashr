import sys


letters = {
    "1": ["a", "k"],
    "2": ["b", "l"],
    "3": ["c", "m"],
    "4": ["d", "n"],
    "5": ["e", "o"],
    "6": ["f", "p"],
    "7": ["g", "q"],
    "8": ["h", "r"],
    "9": ["i", "s"],
    "0": ["j", "t"],
}


def hashr(string: str) -> str:
    total = 0
    primes = [5, 11, 31, 127, 709, 5381, 52711, 648391]
    point = 7

    for char in string:
        total += ord(char)
        total *= primes[point]
        point -= 1 if point > 0 else -7

    total_string = ""
    flip = 0
    for num in str(total):
        total_string += letters[num][flip]
        flip = 1 - flip
    return total_string


if __name__ == "__main__":
    # this doesn't change similar character values
    # enough, needs more complexity, possibly modulo?
    print(hashr(sys.argv[1]))
