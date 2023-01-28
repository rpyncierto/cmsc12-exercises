#This function redirect the program's action based on the user's selection.
def menu(z):
    if z == 1:
        print("The sum of the squares of all even integers from 1 to", x, "is", getSummation(x))
        return True
    elif z == 2:
        getBox(y)
        return True
    elif z == 3:
        print("The average of odd integers from 1 to", x, "is", getAverage(x))
        return True
    elif z == 0:
        print("Goodbye! Have a great day!")
        exit()
    else: 
        print("Invalid input")

#This function determines whether or not the user's input is valid based on the given criteria, where x must be an even integer, y must be an odd integer, and both must be positive integers.
def is_valid_input(x, y):
    if x < 0 or y < 0:
        print("x and y must be both POSITIVE integers!")
        print()
        return False
    elif not is_even_integer(x):
        if not is_odd_integer(y):
            print("x must be EVEN integer and y must be ODD integer!")
        else:
            print("x must be EVEN integer!")
        print()
        return False    
    elif not is_odd_integer(y):
        print("y must be ODD integer!")
        print()
        return False
    else:
        print()
        return True

#This function determines whether the user's input for x value is an even integer or not.
def is_even_integer(x):
    if x % 2 == 0:
        return True

#This function determines whether the user's input for y value is an odd integer or not.
def is_odd_integer(y):
    if y % 2 != 0:
        return True

#This function computes and returns the sum of the squares of all non-negative even integers from 1 to x.
def getSummation(x):
    sum = 0
    for i in range (1, x+1):
        if is_even_integer(i):
            sum += i ** 2
    return sum

#This function returns the NxN pattern where y equals N.
def getBox(y):
    for j in range(y):
        for i in range(y):
            print("* ", end = "")
        print()      

#This function computes and returns the average of odd integers from 1 to x.
def getAverage(x):
    average = 0
    count = 0
    for i in range(1, x+1):
        if is_odd_integer(i):
            average += i
            count += 1
    return average/count

#This is the main progra. This organizes the functionality of the functions.
while True:
    x = int(input("Enter value for x: "))
    y = int(input("Enter value for y: "))
    while is_valid_input(x, y):
        print("Please choose from the following:", "1. Summation", "2. Box", "3. Average", "0. Exit", sep = "\n")
        z = int(input("Enter your choice: "))
        print()
        menu(z)