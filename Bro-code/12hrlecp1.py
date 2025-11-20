#Introduction
#print("Hello world it's me praj, tryna learn python")

#VARIABLES = A container for value )string,integer, float, boolean )
            #A variable behaves as if it was the value it contains

food= "masala dosa" 
#print(f"I like {food}")

#integers 
age =19
#print(f" I am {age} years old ")
 
quantity = 3 
#print(f"you are buying {quantity} sets of cloths for your college") 

num_of_students= 63
#print(f"Your class has {num_of_students} students")

#Float 
price = 10.99
gpa = 8.6
distance = 3.5

#print(f"I walk {distance}km everyday")

#Boolean 
for_sale = False
# if for_sale:
#     print("that item is available")
# else: 
#     print("that item is not available")
#     EncodingWarning

#Type casting = the process of converting a variable from on data type to another str(),int(),float(),bool()
name= "PRAJWAL"
age= 19
gpa = 8.6
is_student= True


age = str(age)
age+="1"
#print(age)

name = bool(name)
#print(name)

#INPUT()= A function that prompts the user to enter data Returns the entered data as a string

# name = input("What is your name?:")
# age = int(input("How old am I : "))

# age = age + 1

# print(f"Hello {name}!")
# print(f"You are {age} years old")

#Arthematic operators + - * / % ** //
friends = 5
#instead of friends = friends -2 
#use
friends -= 2 #subtraction operator
friends += 3 #addition operator
friends *= 5 #multiplication operator
friends /= 3 #division operator
friends = friends**2 #exponentiation operator
remainder = friends % 3  #modulus operator

#print(remainder) 

x = 3.14
y = -4
z = 5

result = round(x)
result = abs(y)
result = pow(4,3) #power function 4^3
result = max(x,y,z)
result = min(x,y,z)

#print(result)

import math 

a = 3.9

# print(math.pi)
# print(math.e)

answer = math.ceil(a) #rounds up
answer = math.floor(a) #rounds down

#print(answer)


#If   = Do some code only IF some condition is True
#Else = Else do something else 
#Elif = A block of code that will execute if the previous conditions were False and this condition is True 


#age = int(input("Enter your age: "))
# if age >= 65:
#     print("You are too old gramps/granny")   
# elif age >= 18:
#     print("You are now signed up")
# elif age <0:
#     print("You havent been born yet")
     
# else: 
#     print("You must be at least 18 to sign up")    

# response = input("would you like some food? (yes/no): ")
# if response == "yes": #the == is the variable comparison operator
#     print("Here is some food")
# else:
#     print("No food for you")

name = input("Enter your name: ")
if name == "":
    print("You did not enter a name")
else:
    print(f"Hello {name}!")

#PART 1 OF THE 12HR LEC IS COMPLETE     