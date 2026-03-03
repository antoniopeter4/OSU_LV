
try:
    num=float(input("Enter a number between 0.0 and 1.0:"))
    if num<0.0 or num>1.0:
        print("Invalid number entered!")
    
    elif num>=0.9:
        print("A")
    elif num>=0.8:
        print("B")
    elif num>=0.7:
        print("C")
    elif num>=0.6:
        print("D")
    else:
        print("F")
except:
    print("Number not entered!")