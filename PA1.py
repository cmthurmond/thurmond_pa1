# Programmers: Cierra Thurmond
# Course: CS151, Professor Franceshci
# Date: September 19, 2017
# Programming Assignment: PA1
# Problem Statement: To calculate the square footage of a room and use that calculation to compute the price it would \
# cost to purchase the necessary amount of carpet to re-carpet the room.
# Data In: length of the room, width of the room, price of carpet per square foot
# Data Out: area of room, total price to buy carpet
# Other files needed: none
# Credits: none

print ("This program will calculate the square footage of a room and use that calculation to compute the price it would"
       " cost to purchase the necessary amount of carpet needed.")

#Get user input for length of the room
room_length = input ("What is the length of the room?")
room_length = int (room_length)

#Get user input for length of width of the room
room_width = input ("What is the width of the room?")
room_width = int (room_width)

#Calculate the area, in square feet, of the room
room_area = room_length*room_width
print ("The area of the room is", room_area, "square feet.")

#Get user input for the price of the carpet per square foot
carpet_price = input ("How much does the carpet cost per square foot?")
carpet_price = float (carpet_price)

#Calculate the total price to purchase the necessary amount of carpet needed
total_price = carpet_price*room_area
print ("The total price to purchase carpet for this room is $",total_price)

#Output the area of the room and the total price to purchase the carpet