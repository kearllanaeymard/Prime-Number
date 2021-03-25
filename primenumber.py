num = int(input("Input a number: "))
for i in range(2, num+1):
    for j in range(2, i):
        if i % j == 0:
            break
    else:
        x = i

newNum = num
while True:
    newNum += 1
    for k in range(2, newNum):
        if newNum % k == 0:
            break
    else:
        y = newNum
        break


if (num - x) <= (y - num):
    print(f"{x} is the nearest prime number of {num}.")
else:
    print(f"{y} is the nearest prime number of {num}.")
