# factorial of a number
num = int(input("Enter the value for which you need factorial "))
fact = 1
i = 1
while i <= num:
    fact = fact * i
    i = i + 1
print("factorial for ", num , "is" , fact)



