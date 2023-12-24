import sys


letters = {
    '1': 'a',
    '2': 'b',
    '3': 'c',
    '4': 'd',
    '5': 'e',
    '6': 'f',
    '7': 'g',
    '8': 'h',
    '9': 'i',
    '0': 'j'
}

def hashr(string):
    total = 0
    primes = [5, 11, 31, 127, 709, 5381, 52711, 648391]
    point = 0
    
    for char in string:
        total += ord(char)
        total *= primes[point]
        point += 1 if point < 7 else -7

    total_string = ''.join([letters[num] for num in str(total)])
    return total_string


if __name__ == "__main__":
    print(hashr(sys.argv[1]))
