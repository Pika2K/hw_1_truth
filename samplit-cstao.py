import random
import sys
file = sys.argv[1]

with open(file, "r") as f:
    for line in f:
        if random.random() < 0.01:
            print(line.strip())
