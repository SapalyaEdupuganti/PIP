#variables/datatypes
name = input("Enter your name: ")
age = int(input("enter your age: "))
height = float(input("Enter your height in meters: "))
city = input("enter your city name: ")
print(f"My name is {name},my age is {age},my height is {height} meters and i live in {city}.")

#--------------------------------------------------------------------------------------------------

#Operations
a = 11
b = 25
c = 22
print("sum of the nubers is: ", a+b+c)
print("Differnence of the numbers is:",a-b-c)
print("product of the nmbers is :",a*b*c)
print("Division of the numbers is:",a/b/c)

#--------------------------------------------------------------------------------------------------


length = int(input("enter the length of the rectangle: "))
width = float(input("enter the width of the rectangle:"))
area= length*width
perimeter = 2 * (length + width)
print("Area of the rectangle is:",area)
print("Perimeter of the rectangle is:",perimeter)


#----------------------------------------------------------------------------------------------------

#conditions
temperature = 32
if temperature < 0:
    print("It's cold")
elif temperature >35:
    print("it's Hot")
else:
    print("it's moderate")


#----------------------------------------------------------------------------------------------------

name = input("Enter the student's name: ")
mark1 = int(input("Enter mark for subject 1: "))
mark2 = int(input("Enter mark for subject 2: "))
mark3 = int(input("Enter mark for subject 3: "))

total = mark1 + mark2 + mark3
average = total / 3

if mark1 >= 35 and mark2 >= 35 and mark3 >= 35 and average >= 50:
    result = "Pass"
else:
    result = "Fail"

print(f"{name}: total = {total}, average = {average:.2f}, result = {result}")