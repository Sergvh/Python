num = int(input("Enter number please:"))
count = 0
for j in range(2, num+1, 1):
    for i in range(2,num,1):
        if num % i == 0:
            count += 1
    if count==0:
        print(str(num))
    count = 0
    num -=1