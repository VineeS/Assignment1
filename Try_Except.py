# When we use Try it does not stops when the error occurs just runs the except code
astr = " Hello World"
try:
    istr = int(astr)
except:
    istr = -1
print("first", istr)


aaa = 123
try:
    bbb = int(aaa)
except:
    bbb = -1
print("Second", bbb)


bbb = "Vinee"
try:
    print("Hello")  # It will execute this statement
    ccc = int(bbb)  # This wont execute
    print("Executed")
except:
    ccc = -1
print("Third", ccc)


num = input("Enter the number")
try:
    New = int(num)
except:
    New = -1

if New > 0:
    print("Correct number")
else:
    print("Not a valid number")
