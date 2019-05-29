import math
max_num = int(input("Max Number"))
primes = [2]
test_num = 3

while test_num < max_num:
    i = 0
    while primes[i] < math.sqrt(test_num):
        if (test_num % primes[i]) == 0:
            test_num += 1
            break
        else:
            i += 1
    else:
        primes.append(test_num)
        test_num += 1
print(primes)
