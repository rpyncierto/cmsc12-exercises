#This program asks for grades and the number of units of each course taken by students to compute their GWA.
#This program converts grade input to a float and the number of units input to an integer.



grade_first = float(input("Enter grade:\n")) #insert a new line, ask for a grade, convert it to a float

units_first = int(input("Enter number of units:\n")) #insert a new line, ask for the number of units, convert it to an integer


grade_second = float(input("Enter grade:\n")) 

units_second = int(input("Enter number of units:\n")) 


grade_third = float(input("Enter grade:\n")) 

units_third = int(input("Enter number of units:\n")) 
 

grade_fourth = float(input("Enter grade:\n")) 

units_fourth = int(input("Enter number of units:\n")) 


grade_fifth = float(input("Enter grade:\n")) 

units_fifth = int(input("Enter number of units:\n")) 



total_units = units_first + units_second + units_third + units_fourth + units_fifth #total units taken by students



GWA = ((grade_first * units_first) + (grade_second * units_second) + (grade_third * units_third) + (grade_fourth * units_fourth) + (grade_fifth * units_fifth)) / total_units #this calculates the students' GWA.



#This prints the GWA of the students as well as the corresponding latin honor if the student can maintain the GWA for all courses.

if  GWA <= 1.20: 
	print("Your GWA is", round(GWA, 4), ".") #print the string, round the GWA into 4 decimal places
	print("If you can maintain your GWA you can graduate summa cum laude.")


elif 1.45 >= GWA > 1.20:
	print("Your GWA is", round(GWA, 4), ".")
	print("If you can maintain your GWA you can graduate magna cum laude.")


elif 1.75 >= GWA > 1.45:
	print("Your GWA is", round(GWA, 4), ".")
	print("If you can maintain your GWA you can graduate cum laude.")


else: #GWA > 1.75 
	print("Your GWA is", round(GWA, 4), ".")
	print("Improve your GWA to receive latin honors.")



