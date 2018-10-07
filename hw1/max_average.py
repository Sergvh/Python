sum = 0
count = 0
i = 0
while (i in range(0,1000000000000,1)):
    s = input("\n Enter number between 1 and 1000000000000 or not number for exit:")
    if s.isdecimal():
        sum += int(s)
        i = int(s)
        count += 1
    else:
        break

print("The Average is - "+str(sum/count))
