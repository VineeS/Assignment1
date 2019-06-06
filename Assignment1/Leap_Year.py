# Find if the year is leap year or not
year = int(input("Enter the year"))
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("{0} Leap year".format(year))
        else:
            print(" {0} Not a Leap year".format(year))
    else:
        print("{0} Leap year".format(year))
else:
    print("{0} Not a Leap Year".format(year))
