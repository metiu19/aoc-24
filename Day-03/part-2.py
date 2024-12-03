import re

with open('input') as f:
    lines = f.readlines()
    sum = 0
    do = True
    for line in lines:
        matches = re.findall(r"mul\(([0-9]{1,3}),([0-9]{1,3})\)|(do\(\))|(don't\(\))", line)
        print(matches)
        for match in matches:
            if (match[3] != ''):
                do = False
            elif (match[2] != ''):
                do = True
            elif (do):
                sum += int(match[0]) * int(match[1])
                print("Partial: ", sum)

    print("Total: ", sum)
