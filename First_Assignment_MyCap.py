#Problem 1
#This program takes input from the user and calculates radius
R = int(input("Enter your number: "))
var1 = (22/7) * (R ** 2)
print(var1)

#Problem 2
#This program prints the extension of a given file
filename = input("Enter the filename: ")
file_extension = filename.split(".")
print("The extension is: " + (file_extension[-1]))
