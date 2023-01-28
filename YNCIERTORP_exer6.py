# This function shows the menu that redirect the program's action based on the user's selection.
def showMenu():
    print("Options:", "[1] Add a member", "[2] View a member record", "[3] View all members", "[4] Delete a member record",
          "[5] Delete all member records", "[6] Save to file", "[7] Load from file", "[0] Exit", sep="\n")
    choice = int(input("Choice: "))
    return choice

# This function computes and returns the bmi of the user-inputted member.


def BMI(weight, height):
    bmi = round(weight / (height / 100) ** 2, 1)
    if bmi % 1 == 0:
        bmi = round(bmi)
    else:
        bmi
    return bmi

# This function categorizes the member's bmi based on the interval equivalent of each type.


def BMICategory(bmi):
    if bmi < 18.5:
        category = "Underweight"
    elif 18.5 <= bmi <= 24.9:
        category = "Normal"
    elif 25 <= bmi <= 29.9:
        category = "Overweight"
    elif bmi >= 30:
        category = "Obese"
    return category

# This function assigns an auto-increment member ID to each member.


def memberID(name):
    ID = memberNames.index(name) + 1
    while len(str(ID)) < 3:
        ID = "0" + str(ID)
    ID = "M" + ID
    return ID

# This function converts the float height and weigth values into a string for concatenation.


def floatToString(x):
    x = round(x, 1)
    if x % 1 == 0:
        x = round(x)
    else:
        x
    return str(x)

# This function adds a member to the application and assigns a unique member ID to them.


def addMember():
    memberName = input("Enter name: ")
    memberWeight = float(input("Enter weight (kg): "))
    memberHeight = float(input("Enter height (cm): "))
    bmi = BMI(memberWeight, memberHeight)
    category = BMICategory(bmi)
    print("BMI is", bmi)
    print("Type is", category)
    memberWeight = floatToString(memberWeight)
    memberHeight = floatToString(memberHeight)
    record = memberWeight, memberHeight, str(bmi), category
    memberRecord = {}
    memberRecord[memberName] = record
    memberNames.append(memberName)
    ID = memberID(memberName)
    allMembers[ID] = memberRecord
    return allMembers[ID]

# This function displays the member's record based on the member ID entered by the user.


def viewRecord():
    ID = input("Enter member id: ")
    if ID not in allMembers:
        print("Sorry, the record does not exist!")
    else:
        print("=== Member Information ===")
        print("(", ID, ")", sep="", end=" ")
        for k in allMembers[ID]:
            memberRecord = allMembers[ID]
            print(k, end=" ")
            units = ["kg", "cm", "(BMI:", ";", ")"]
            for i in range(0, 2):
                print(memberRecord[k][i], units[i], end=" ")
            for l in range(2, len(memberRecord[k])):
                print(units[l], memberRecord[k][l], end="")
            print(units[len(units)-1])

# This function displays all of the members that have been saved in the application.


def viewAllMembers():
    print()
    print("=== List of members ===")
    count = 1
    for ID in allMembers:
        print(count, ". ", "(", ID, ")", sep="", end=" ")
        for k in allMembers[ID]:
            memberRecord = allMembers[ID]
            print(k, end=" ")
            units = ["kg", "cm", "(BMI:", ";", ")"]
            for i in range(0, 2):
                print(memberRecord[k][i], units[i], end=" ")
            for l in range(2, len(memberRecord[k])):
                print(units[l], memberRecord[k][l], end="")
            print(units[len(units)-1])
        count += 1

# This function deletes a specific member record based on the member ID entered by the user.


def deleteRecord():
    ID = input("Enter member id: ")
    if ID not in allMembers:
        print("Sorry, the record does not exist!")
    else:
        del allMembers[ID]
        print("Member", ID, "successfully deleted.")

# This function removed all members from the application's database.


def deleteAllMembers():
    allMembers.clear()
    print("All entries successfuly deleted")

# This function saves all information for each fitness club member in a csv file.


def saveFile():
    fileWriter = open("members.csv", "w")
    count = 0
    for ID in allMembers:
        for k in allMembers[ID]:
            memberRecord = allMembers[ID][k]
            record = ""
            for i in range(0, len(memberRecord)):
                if i < len(memberRecord) - 1:
                    record += str(memberRecord[i]) + "<#>"
                else:
                    record += str(memberRecord[i])
            fileWriter.write(ID + "<#>" + k + "<#>" + record + "\n")
        count += 1
    fileWriter.close()
    print("Successfully saved to file (" + str(count) + " entries)")

# This function reads the saved data from the csv file containing the information for each fitness club member.


def loadFile():
    fileReader = open("members.csv", "r")
    allMembers.clear()
    count = 0
    for line in fileReader:
        line = line[:-1].split("<#>")
        index = 0
        ID = line[index]
        memberName = line[index + 1]
        memberWeight = line[index + 2]
        memberHeight = line[index + 3]
        bmi = line[index + 4]
        category = line[index + 5]
        record = memberWeight, memberHeight, str(bmi), category
        memberRecord = {}
        memberRecord[memberName] = record
        memberNames.append(memberName)
        allMembers[ID] = memberRecord
        count += 1
    fileReader.close()
    print("Successfully loaded entries from file (" + str(count) + " entries)")

# This function exits the application if the user wishes to stop using it.


def Exit():
    print()
    print("Thank you for using this program!")
    exit()


# This part shows the empty list and dictionary used in the application.
allMembers = {}
memberNames = []

# This part is the main program of the application. This organizes the functionality of the functions.
print("Welcome to CMSC Fitness Club")
while True:
    c = showMenu()

    if c == 1:
        addMember()

    elif c == 2:
        viewRecord()

    elif c == 3:
        viewAllMembers()

    elif c == 4:
        deleteRecord()

    elif c == 5:
        deleteAllMembers()

    elif c == 6:
        saveFile()

    elif c == 7:
        loadFile()

    elif c == 0:
        Exit()

    else:
        print("Invalid input")

    print()
