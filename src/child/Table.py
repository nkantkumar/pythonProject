#Python program to display multiplication table

#Get the number from the user for multipication table
tab_number = int(input ("Enter the number of your choice to print the multiplication table: "))

#For loop to iterate the multiplication 10 times and print the table
print ("The Multiplication Table of: ", tab_number)
for count in range(1, 11):
   print (tab_number, 'x', count, '=', tab_number * count)