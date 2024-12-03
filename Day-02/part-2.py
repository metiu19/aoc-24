def checkLevel(l, lNext, inc):
    error = ((l > lNext) and inc) or ((l < lNext) and not inc)
    delta = abs(l - lNext)
    error = error or (delta < 1 or delta > 3)
    return error

def checkReport(report):
    good = True
    for i in range(0, len(report) - 1):
        increasing = report[0] < report[1]
        if (checkLevel(report[i], report[i + 1], increasing)):
            good = False
            return good
    return good

with open('input') as f:
    lines = f.readlines()
    reports = []

    for line in lines:
        reports.append([int(item.strip()) for item in line.split(" ")])

num = 0
for report in reports:
    print(report)

    good = checkReport(report)
    if (not good):
        for i in range(len(report)):
            print("i: ", i)
            copy = report.copy()
            item = copy.pop(i)
            print(copy)
            good = checkReport(copy)
            print(good)
            if (good):
                print("Wrong level: ", item)
                break;

    if (good):
        print("Report good")
        num += 1
    print("Good reports: ", num, "\n")

