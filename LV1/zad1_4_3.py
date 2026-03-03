numbers=[]
num=""

while (num!="Done"):
    num=input("Enter a number:")
    #if not(num.isdigit()):
       # print("Invalid Enter! Not a number")
    #else:
        #numbers.append(num)
   
    if (num=="Done"):
        break
    
    try:
        number=float(num)
        numbers.append(number)

    except:
       print("Invalid Enter! Not a number")


print(numbers)
print("Number of numbers:",len(numbers))
print("Max:",max(numbers))
print("Min:",min(numbers))
print("Avg:",sum(numbers)/len(numbers))
print("Sorted:",numbers.sort)
