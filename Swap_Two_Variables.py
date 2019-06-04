i = 0
j = 0
Var1 = input("Enter Var1")
Var2 = input("Enter Var2")
i = Var1
j = Var2
Var1 = j
Var2 = i
print("new value of Var1",Var1 , "New Value of Var2", Var2)


Var1 = input("Enter Var1")
Var2 = input("Enter Var2")
temp = Var1
Var1 = Var2
Var2 = temp
print("Value After swap var 1 {}", format(Var1))
print("Value After Sawp var 2 {}", format(Var2))