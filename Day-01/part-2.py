with open('input') as f:
    lines = f.readlines()
    ll = []
    lr = []

    for line in lines:
        line = line.strip()
        data = [item.strip() for item in line.split(' ')]
        ll.append(int(data[0]))
        lr.append(int(data[3]))

ll.sort()
lr.sort()
sim = 0

for item in ll:
    x = lr.count(item)
    sim += (item * x)

print(sim)
