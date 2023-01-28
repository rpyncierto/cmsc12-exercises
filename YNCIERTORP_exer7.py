#Good day Maam, I have modified the spacing of each display of the output of functions for readability.

#This function creates two one-dimensional vectors.
def makeVector():
    for i in range(n):
        x = int(input("Enter number for list1: "))
        list1.append(x)
    print("Enter contents for list2")
    for j in range(n):
        y = int(input("Enter number for list2: "))
        list2.append(y)

#This function shows the menu that redirect the program's action based on the user's selection.
def getMenu():
    print("[1] Add Vectors", "[2] Subtract Vectors", "[3] Get summation", "[4] Exit", sep = "\n")
    choice = int(input("Choice: "))
    return choice

#This function adds the elements of two one-dimensional vectors with the same index.
def getSum(lst1, lst2):
    if len(lst1) == 0 or len(lst2) == 0:
        return []
    return [lst1[0] + lst2[0]] + getSum(lst1[1:len(lst1)], lst2[1:len(lst2)])

#This function subtracts the elements of two one-dimensional vectors with the same index.
def getDifference(lst1, lst2):
    if len(lst1) == 0 or len(lst2) == 0:
        return []
    return [lst1[0] - lst2[0]] + getDifference(lst1[1:len(lst1)], lst2[1:len(lst2)])

#This function displays a menu that redirects the program's action based on the user's choice if the user wishes to get the summation of a one-dimensional vector.
def getSummationMenu():
    print("Which list do you want to add?", "[1] List1", "[2] List2", "[3] Go Back to Menu", sep = "\n")
    choice = int(input("Choice: "))
    return choice

#This function calculates the sum of all elements contained within a one-dimensional vector.
def getSummation(list):
    if len(list) == 0:
        return 0
    else :
        return list[0] + getSummation(list[1:len(list)])

#This part contains the lists where the elements of the two one-dimensional vectors will be placed.
list1 = []
list2 = []

#This part is the main part of the program. This organizes the functionality of the functions.
n = int(input("How many items to be placed in the list? "))
makeVector()
while True:
    print()
    c = getMenu()
    print()
    if c == 1:
        print("The sum of two vectors is", getSum(list1, list2))
    elif c == 2:
        print("The difference of two vectors is", getDifference(list1, list2))
    elif c == 3:
        choice = getSummationMenu()
        if choice == 1:
            print()
            print("The summation of list1 is:", getSummation(list1))
        elif choice == 2:
            print()
            print("The summation of list2 is:", getSummation(list2))
        elif choice == 3:
            continue
        else:
            print("Invalid Input")
    elif c == 4:
        exit()
    else:
        print("Invalid input")
