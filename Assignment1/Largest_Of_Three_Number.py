# Find largest of three numbers
num1 = input("Number 1")
num2 = input("Number 2")
num3 = input("Number 3")
if num1 > num2 and num1 > num3:
    largest = num1
elif num2 > num1 and num2 > num3:
    largest = num2
elif num3 > num1 and num3 > num2:
    largest = num3
print("The greatest number is ", largest)


