a = []

for i in range(1500, 3000, 1):
    if i % 7 == 0 and i % 3 != 0:
        a.append(i)

print(a)
