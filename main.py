print("Hello World")

name = input("Enter your name:")
time = float(input("Enter the current time:"))
if(time>12.00):
  print("good afternoon",name)
elif(time<12.00):
  print("good morning",name)
else:
  print("good night",name)