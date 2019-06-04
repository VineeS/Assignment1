Hours = input(" Enter the hours for work ")
Rate = input(" Enter the rate per hour ")
try:
    Amount = float(Hours)*float(Rate)
except:
    Amount = -1

if Amount > 0:
    print("Total Amount :", Amount)
else:
    print("Please Enter numeric Value")

