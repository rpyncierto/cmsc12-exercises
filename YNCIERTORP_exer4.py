# This function removes the characters that are common to both names or strings and returns the characters that are left.
def removeChar(name1, name2):
    newstr = ""
    for x in name1:
        if x not in name2:
            newstr = newstr + x
    return newstr

# This function returns the total number of characters left after removing the common characters from the two strings or names.
def countRemainingChar(name1, name2):
    total = len(name1 + name2)
    return total

# This function is responsible for removing the Nth item from the list indefinitely until only one item remains, at which point it returns the item remaining.
def assignCategory(category, total):
    while len(category) > 1:
        index = (total % len(category)-1)
        if index >= 0:
            right = category[index + 1:]
            left = category[:index]
            category = right + left
        else:
            category = category[:len(category)-1]
    return category

# This function converts the left item in category into its relationship list equivalent and returns it.
def convertToRelationship(category, result, relationship):
    newIndex = ""
    for value in result:
        newIndex += value
    index = category.index(newIndex)
    relationship = relationship[index]
    return relationship

# This section contains the lists from which the relationship of both string names will be derived.
category = ["K1", "K2", "K3", "K4", "K5", "K6"]
relationship = ["Kaibigan", "Kapuso", "Kaaway", "Kasal", "Kilig(Crush)", "Kapatid"]

# This section lowercases the string or names entered by the user.
name1 = input("Player 1 name : ").lower()
name2 = input("Player 2 name : ").lower()

# This section removes any spaces from the user-entered strings or names.
name1 = name1.replace(" ", "")
name2 = name2.replace(" ", "")

# This section involves using the removeChar function to remove the common characters from both string or names.
newStr1 = removeChar(name1, name2)
newStr2 = removeChar(name2, name1)

# This section uses the countRemainingChar function to count the remaining characters in strings or names and stores the results in a variable called total.
total = countRemainingChar(newStr1, newStr2)

# Using the assignCategory function, this section removes the Nth item from the list until only one item remains, and stores it in a variable called result.
result = assignCategory(category, total)

# Using the convertToRelationship function, this section converts the category result to its equivalent item in the relationship list and prints it.
print("Relationship status :", convertToRelationship(category, result, relationship))