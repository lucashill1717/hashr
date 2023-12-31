def number_to_letters(number: int) -> str:
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
    
    chars = []
    flip = 0
    for num in str(number):
        chars.append(letters[num][flip])
        flip = 1 - flip
    return "".join(chars)


def saltr(letters=False) -> int:
    """
    salt
    """

    from random import randint

    return randint(1000000, 9999999)


def hashr(input: str, use_salt=False) -> str | list[str]:
    """
    remember to document
    """

    if len(input) == 0:
        return ""

    def hash(string: str, current_sum: int) -> int:
        primes = [5, 11, 31, 127, 709, 5381, 52711, 648391]
        point = 7

        for char in string:
            current_sum += ord(char)
            current_sum *= primes[point]
            point -= 1 if point > 0 else -7
        return current_sum

    total = 0
    total += hash(input, total)
    total += hash(str(total), total)
    total %= 10888869450418352160768000001

    return number_to_letters(total)


def _main():
    from argparse import ArgumentParser

    parser = ArgumentParser(description="testing")  # fill out more fields here
    parser.add_argument("input", help="string")
    parser.add_argument("-s", "--use-salt", action="store_true", help="salt")
    args = parser.parse_args()
    print(hashr(args.input, args.use_salt))


if __name__ == "__main__":
    _main()
