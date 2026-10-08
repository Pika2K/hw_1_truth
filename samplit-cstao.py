import random
import sys
file = sys.argv[1]
msg = "trivial change in file in hw_1a!"
message = "small change in script in hw_1b"

with open(file, "r") as f:
    for line in f:
        if random.random() < 0.01:
            print(line.strip())
