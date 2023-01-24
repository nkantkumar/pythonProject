num1 = input('Enter first number: ')
num2 = input('Enter second number: ')
sum = num1 + num2
print('The sum of the numbers is', sum)


num1 = input('Enter the first number: ')
num2 = input('Enter the second number: ')

# Converting and adding two numbers using int() & float() functions
sum = (num1) + int(num2)

# Subtracting the two numbers
sub = int(num1) - int(num2)

# Multiplying two numbers
mul = float(num1) * float(num2)

#Dividing two numbers
div = float(num1) / float(num2)


# Displaying the results of arithmetic operations
print('The sum of {0} and {1} is {2}'.format(num1, num2, sum))


#Python program to check whether the given year is leap year or not

# Function implementation to check leap year
def LeapYear(Year):
  #Condition to check if the given year is leap year or not
  if((Year % 400 == 0) or
     (Year % 100 != 0) and
     (Year % 4 == 0)):   
    print("The given Year is a leap year");
  # Else it is not a leap year
  else:
    print ("The given Year is not a leap year")
# Taking an input year from user
Year = int(input("Enter the year to check whether a leap year or not: "))
# Printing the leap year result
LeapYear(Year)
