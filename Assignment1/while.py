n = 0
while (n<20):
    n = n+1
    print(n)
print(" order 1 ")
# bigger value to smaller

x = 20
while (x>0):
    print(x)
    x = x-1

print(" order 2 ")
# smaller to bigger

x = 10
y = 100
x = 25  # latest value of x
print(x)
print(y)

i = 5
x = 3.15 * i * (i - 1)
print(x)
# also we can have x = 3.15 * x * (x - 1)
# goes left to right ie first i-1 then * i ..
# ** is to the power
print(9/2)

ddd = "Hello" +  " There"  # string concatenation
print(ddd)

print(" Hello " * 3)  # Repeats the str 3 times


ccc = 4 + 2
print(ccc)

# Gives the data tyoe
xx = 2
print(type(xx))
yy = 2.2
print(type(yy))
zz = "vinee"
print(type(zz))

# Explicitly change the type
xyz = str(input(print("Enter the number :")))
zyx = float(input(print("Enter the decimal number :")))
yzx = input(print("Enter the number : "))
# print(zyx + yzx) gives error as yzx takes str value by default
zzz = int(input(print("Enter the value : ")))
print(zyx + zzz)


name = input(print("Enter your name " ))
print('Welcome ' + name)


# european floor and US floors
Europe = int(input(" Enter the floor "))
US = Europe + 1
print("Us floor ", US) # print the Updated value in US





