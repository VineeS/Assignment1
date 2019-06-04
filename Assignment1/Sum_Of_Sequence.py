# Sum of numbers means if we enter 5 then 1+2+3+4+5 = 15
num = int(input("Enter the number :"))
i = 0
j = 0
while i <= num:
    k = i + j
    j = k
    i = i + 1
print("sum of numbers", k)
