
#!/usr/bin/python
a = input("How many apples do you got?\n")
try:
    a = int(a)
except:
    print("\33[41m[error]\33[0m",a,"NAN")
else:
    print("You got ", a ," apples!")
b = input("How many bananas do you got?\n")
try:
    b = int(b)
except:
    print("\33[41m[error]\33[0m",b,"NaN")
else:
    print("You got ", b ," apples!")
