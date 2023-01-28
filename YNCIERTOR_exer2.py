# This program asks for two integers n and m, and print the sum of all 
#	(a) even numbers between n and m (n and m are included)
#	(b) odd numbers between n and m (n and m are included)

# initialization part of the program (initial value of the variables even and odd)
even = 0
odd = 0

n = int(input("Enter an integer:\n"))			# insert a new line, ask for an integer, convert it to an integer and store it in variable n
m = int(input("Enter another integer:\n"))		# insert a new line, ask for an integer, convert it to an integer and store it in variable m

if n > m:										# condition, check if n, the first integer is greater than m, the second integer
	l = n + m 									# if true, this part will swap or interchange the values of n and m using arithmetic expressions
	n = l - n
	m = l - n
												# using n, m = m, n is also possible

#this part of the program reads whether the two integers are equal or not, if not, through for loop and arithmetic expression, the terminal will read if the dividend variable is an odd or an even number
if n == m:										# condition, check if both integers or n and m are equal
	print("The two integers cannot be equal.")	# if true, it will print that the two integers cannot be equal
else:											# if false or n is not equal to m or both integers are not the same
	for dividend in range(n, m + 1):			# for loop, dividend variable is the sequence of numbers starting from n, the first integer, to m, the second integer (added with 1 for it to be counted in the range of for loop since for loop is expressed as (start, stop) where it starts from the start and ends with stop - 1)	
		if dividend % 2 == 0:					# condition, check if dividend variable modulo 2 is equal to zero
			even = dividend + even				# if true, initial value of the even variable which is zero is equal to the dividend variable added with the even variable
			continue							# returns the control to the beginning of the loop and rejects the remaining statements in the current iteration
		odd = dividend + odd 					# if divident variable modulo 2 is not equal to zero, initial value of the odd variable which is zero is equal to the dividend variable added with the odd variable
	
# printing the sum of even and odd numbers from n to m (n and m are included) 
	print("The sum of even numbers from", n, "to", m, "is", even)
	print("The sum of odd numbers from", n, "to", m, "is", odd)
