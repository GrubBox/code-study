

import random

filename = input("Filename: ")
with open(filename, "r") as f:
    lines = f.readlines()
    print([line.rstrip() for line in lines])  # Print the original lines without newline characters
    random.shuffle(lines)
    print([line.rstrip() for line in lines])  # Print the shuffled lines without newline characters
with open(filename, "w") as f:
    f.writelines(lines)
