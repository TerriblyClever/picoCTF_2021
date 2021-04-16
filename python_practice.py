#Python has 4 types of data
#Integers, Decimals, Booleans, Strings
#radius = int(input("Please enter a radius: ")) #makes radius an integer
precision = int(input("How precise would you like your answer? "))
radius_2 = 4.3 #makes radius a decimal, or 'float'
radius_3 = 'four' #make radius a string of plain text
radius_4 = True #make the variable a Boolean

"""
counter = 0
while counter < 10:
    area = 3.14159 * (counter**2) # + - / * ** % (modulo, returns the remainder after division)
    print(round(area, precision))
    counter += 1
"""

for number in range(0, 10):
    area = 3.14159 * (number**2) # + - / * ** % (modulo, returns the remainder after division)
    print(round(area, precision))

print("hello")