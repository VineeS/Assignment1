# Armstrong number
n = int(input("value"))

def FirstNumber(n):
       while n >= 10:
            n = n / 10
       return int(n)


def MiddleNumber(n):
    while n >= 10:
        n = n / 10
        n = n % 10
    return int(n)
def LastNumber(n):
       return (n % 10)

def ArmstrongNumber(n):
            Value = FirstNumber(n)**3 + MiddleNumber(n)**3 + LastNumber(n)**3
            print(Value)
            if n == Value:
                  print("Armstrong number")
            else:
                print("Not an Armstrong number")






print("First Number = ", FirstNumber(n),"Middle number = ", MiddleNumber(n) ,"Last Number = ", LastNumber(n),"Armstrong value or not ",ArmstrongNumber(n),end="")







