with open('input') as f:
    lines = f.readlines()
    reports = []

    for line in lines:
        reports.append([int(item.strip()) for item in line.split(" ")])
print(reports)

num = 0
for report in reports:
    print(report)
    good = True
    increasing = report[0] < report[1]
    print(increasing)
    for i in range(0, len(report) - 1):
        print(report[i], report[i + 1])
        if ((report[i] > report[i + 1]) and increasing):
            print("Dec when inc")
            good = False
            break
        elif ((report[i] < report[i+1]) and not increasing):
            print("Inc when dec")
            good = False
            break
        delta = abs(report[i] - report[i + 1])
        print(delta)
        if (delta < 1 or delta > 3):
            print("Delta not good")
            good = False
            break
    if (good):
        print("Report good")
        num += 1
    print(num)

print(num)
