n = int (input(" "))
x = n
rev = 0
while(n > 0):
    y = n % 10
    rev = rev * 10 + y
    n = n//10
if (x == rev):
    print("yes")
else:
    print ("no")
