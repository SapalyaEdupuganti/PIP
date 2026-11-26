#sets
'''numbers={1,1,2,2,3,4,5,6,7,8,9}
print(numbers)  # Output: {1, 2, 3, 4, 5, 6, 7, 8, 9} (duplicates removed)

#set operations
A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}
print(A.union(B))  # Output: {1, 2, 3, 4, 5, 6, 7, 8}
print(A.intersection(B))  # Output: {4, 5}  
print(A.difference(B))  # Output: {1, 2, 3}
print(B.difference(A))  # Output: {6, 7, 8}'''

#-------------------------------------------------------------------------------------------
#dictionary
'''student = {"name": "Kowsi", "age": 20, "grade": "A"}
print("student name:", student["name"])  # Output: Kowsi
print("student age:", student["age"])  # Output: 20
#modifying & adding to a dictionary
student["age"] = 21
student["city"] = "Chennai"
print("Modified student details:", student)

#-------------------------------------------------------------------------------------------
#strings
message = "Hello World!"
name = 'Kowsi'
multiline = """Nice to meet you """
#Accessing characters in strings
print(name[3])  # Output: s
#Slicing strings
print(message[6:11])  # Output: World
#use of string methods
print(multiline.lower())  # Output: nice to meet you, 
print(name.upper())  # Output: KOWSI
print(message.replace("World", "Python"))  # Output: Hello Python!
print(multiline.split(" "))  # Output: ['Nice', 'to', 'meet', 'you,']'''

#repeating  and concatenating strings
a = "Hello"
b = "World"
print(a + " " + b)  # Output: Hello World(concatenation)
print(a * 3)  # Output: HelloHelloHello(repetition)
#-------------------------------------------------------------------------------------------
