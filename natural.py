num = int (input(" "))
sum = 0
if num < 0:
    print("Invalid")
else:
    while (num > 0):
        sum += num
        num -= 1
    print(sum)
    
