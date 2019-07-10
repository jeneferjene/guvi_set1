in_num = input()
try:
  inp_num=int(in_num)
  if(inp_num%2)==0:
    print("Even")
  else:
    print("Odd")
except ValueError:
    print("Invalid")
