#!/usr/bin/python
a = input("How many apples do you got?\\n")
print("You got " + a + " apples!")
b = input("How many bananas do you got?\\n")
print("You got " + b + " bananas!")
try:
    total = int(a) + int(b)
    print("You got " + str(total) + " fruits!")
except Exception as e:
    traceback.print_exc()
