import re

with open('input') as f:
    lines = f.readlines()
    sum = 0
    for line in lines:
        matches = re.findall(r"mul\(([0-9]{1,3}),([0-9]{1,3})\)", line)
        for match in matches:
            sum += int(match[0]) * int(match[1])
            print("Partial: ", sum)

    print("Total: ", sum)
