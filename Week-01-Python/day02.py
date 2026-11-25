#loop
#for loop
#Print the even numbers from 2 to 20 and find their total.
total  = 0
for number in range(2,21,2):
    print (number)
    total += number
print("Total of even numbers from 2 to 20 is:", total)

# while loop
# Keep asking for a number until the user enters a positive number.
number = 0
while number <= 0:
    number = int(input("Enter a positive number: "))
print ("your number is:", number)

#nested loop
# print an multipication table for number 1 to 5
for row in range(1,6):
    for column in range(1,6):
        product = row * column
        print(f"{row} * {column} = {product}")
#------------------------------------------------------------------------------
#functions
# calculates the square of a number
def calculate_square(number):
    return number * number

value = float(input("Enter a number: "))
answer = calculate_square(value)

print("The square is:", answer)

#---------------------------------------------------------------------------

