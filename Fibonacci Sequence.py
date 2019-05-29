# 0,1,1,2,3,5,8,13
iteration = 0
i = 0
j = 1
while iteration < 20:
    k = i + j

    i = j
    j = k
    iteration = iteration + 1
    print(i)

print("Fibonacci  series ")