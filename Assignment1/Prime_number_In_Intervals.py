FirstNumber = int(input("Enter the First Number"))
LastNumber = int(input("Enter the last number"))
for num in range(FirstNumber, LastNumber):
 if num > 1:
    for i in range(2, num):

       if (num % i) == 0:
        break
    else:
     print("Prime number", num)

