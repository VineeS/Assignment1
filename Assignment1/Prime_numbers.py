number = int(input("Enter the number"))
if number > 1:
    for i in range(2, number):
        if number % i == 0:
            print("not a prime number ")
            print("number is ", number)
            print("factor is  : ", i)
            break
    else:
        print(number, "is prime")

