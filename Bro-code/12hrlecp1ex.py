#EXCERCISE 1 RECTANGLE AREA CALC

# length = float(input("Enter the length: "))
# width = float(input("Enter the width: "))
# area = length * width

#print(f"The area is :{area}cm²")

#EXCERCISE 2 Shoppign cart program 

# item = input("What item would you like to buy?: ")
# price = float(input("What os the price?: "))
# quantity = int(input("How many would you like?: "))
# total = price * quantity

#print(f"{item} x{quantity} - ${total}")

#MADLIBS GAME
# adjective1=input("Enter an adjective:")
# noun= input("Enter a noun")
# adjective2=input("Enter an adjective:")
# verb= input("Enter a verb")
# adjective3= input("Enter an adjective")

# print(f"Today I went to a {adjective1}zoo.")
# print(f"In an exhibit, I saw {noun}")
# print(f"{noun} was {adjective2} and {verb}ing")
# print(f"I was{adjective3}")  
 
#EXERCISE 4 - ON IMPORT MATH

import math


#radius = float(input("Enter the radius of the circle:")) 

#circumference = 2 *math.pi* radius
#area = 3.14 * radius**2  OR
#area = math.pi *pow(radius,2)
#print(f"The circumference is :{round(area)}cm^2")

a = float(input("Enter the side A: "))
b = float(input("Enter the side B: "))

c = math.sqrt(pow(a,2) +pow(b,2))

print(f"The hypotenuse C is {c}cm ")