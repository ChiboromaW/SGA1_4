# if statement practice



x = int(input("Please input your score:"))
if type(x) == int:

    if x >= 70:
        print("A")
    elif x >= 60 and x <= 69:
        print("B")
    elif x >= 50 and x <= 59:
        print ("C")
    elif x >= 40 and x <= 49:
        print("D")
    else:
        print("Failed")

else:
    print ("our program only accepts interger values")

print("I will execute either way")