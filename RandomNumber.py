# Generate Random number
import random
# import the random module
print("Random number between 0 to 9 : ", end="") # end= is used for the same line
print(random.randint(0,9))
print(random.random()) # generates random number less then 1 and greater or equal to 0
random.seed(4)
print("The mapped random number :", end="")
print(random.random())
random.seed(4)
print("The mapped random number :", end="")
print(random.random())
# Demonstrate the choice(), randrange()
print("Choose from the list : ", end="")
print(random.choice([1, 20, 40, 3]))

print("Random number between 20 to 50 with step size 3:", end="")
print(random.randrange(20, 50, 3))
# This function takes 3 arguments, beginning number (included in generation),
# last number (excluded in generation) and step ( to skip numbers in range while selecting).

