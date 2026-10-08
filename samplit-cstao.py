import random
import sys
file = sys.argv[1]
message = "this message is intended to clash with hw_1b"

with open(file, "r") as f:
    for line in f:
        if random.random() < 0.01:
            print(line.strip())
