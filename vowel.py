while(True):
    ch = input("")
    if((ch >= 'a' and ch <= 'z') or (ch >= 'A' and ch <= 'Z')): 
        if((ch == 'a') or (ch == 'e') or (ch == 'i') or (ch == 'o') or (ch == 'u')): 
            print("Vowel") 
        else:
            print("Consonant") 
    elif(ch >= '0' and ch <= '9'):
        print("invalid")
    else:
        print("invalid")
