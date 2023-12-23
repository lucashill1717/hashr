import sys

def hashr(string):
    total = 0
    prime = 509
    for char in string:
        total += ord(char)
        total *= prime
    total_bytes = total.to_bytes((total.bit_length()+7)//8, "big")
    hexes = [hex(byte) for byte in total_bytes]
    characters = [chr(int(hex, 16)) for hex in hexes]
    print(characters)
    return string

if __name__ == "__main__":
    # reminder to add salt to hash
    print(hashr(sys.argv[1]))
