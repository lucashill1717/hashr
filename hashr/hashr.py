def number_to_letters(number: int) -> str:
    """
    Converts an integer to a string, with characters
    ranging from 'a' to 't'. Used to have a human
    readable hash.

    Parameters:
        - number : integer

    Returns:
        - str : number string converted to letters
    """
    
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


def saltr(letters=True) -> str | int:
    """
    Generates a 7 character salt by default,
    only returning an integer in the millions
    if specified.
    
    Parameters:
        - letters : bool deciding if the salt
        will be characters or not: True == letters,
        False == integer

    Returns:
        - str or int : salt

    A salt is used to increase complexity of a hash.
    Appending 7 random characters to the end of a
    string causes two copies of the same string to have
    entirely different hashes. Just make sure to store
    salts along with their hashes, as otherwise strings
    can no longer be matched to them.
    """

    from random import randint

    number = randint(1000000, 9999999)
    return number_to_letters(number) if letters else number


def hashr(input: str, use_salt=False) -> str | tuple[str, str]:
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

    salt = str(saltr()) if use_salt else ""
    input += salt

    total = 0
    total += hash(input, total)
    total += hash(str(total), total)
    total %= 10888869450418352160768000001

    hashed_string = number_to_letters(total)
    if use_salt:
        return (hashed_string, salt)
    else:
        return hashed_string


def _main() -> None:
    from argparse import ArgumentParser

    parser = ArgumentParser(description="testing")  # fill out more fields here
    parser.add_argument("input", help="string")
    parser.add_argument("-s", "--use-salt", action="store_true", help="salt")
    args = parser.parse_args()

    hash = hashr(args.input, args.use_salt)
    if type(hash) is str:
        print(f"Hash: {hash}")
    else:
        print(f"Hash: {hash[0]}\nSalt: {hash[1]}")


if __name__ == "__main__":
    _main()
