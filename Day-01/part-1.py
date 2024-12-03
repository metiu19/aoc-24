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

out = []
for i in range(len(ll)):
    out.append(abs(ll[i] - lr[i]))

sum = 0

for v in out:
    sum = sum + v

print(sum)
