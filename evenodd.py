ch = input("")
if((ch >= 'a' and ch <= 'z') or (ch >= 'A' and ch <= 'Z')): 
    print("invalid") 
elif(ch >= '0' and ch <= '9'):
    num=int(ch)
    if (num % 2) == 0:
        print("Even")
    else:
        print("Odd")
else:
    print("invalid")
