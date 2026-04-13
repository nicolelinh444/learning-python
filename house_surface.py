# In order to estimate the cost of painting a house, 
# a painter needs to know the surface area of the exterior.
# Write a program that computes the surface area that needs to be painted 
# given the number of windows and doors and the width and the height of each. 
# Assume the windows and doors have a uniform size. Below are the 
# specifications:
# House: Width = 23 ft, length = 45 ft, height = 9.5 ft
# Windows: number of windows = 12, width = 3 ft, height = 3.5 ft
# Doors: number of doors = 4, width = 3, height = 7.5 ft
#
# Don't use magic numbers. Save the values in variables first,
# then do the calculations.

numberOfWindows = 12
windowWidth = 3
windowHeight = 3.5
windowArea = windowWidth * windowHeight
totalWindowArea = numberOfWindows * windowArea

numberOfDoors = 4
doorWidth = 3
doorHeight = 7.5
doorArea = doorWidth * doorHeight
totalDoorArea = numberOfDoors * doorArea

houseWidth = 23
houseHeight = 9.5
houseLength = 45
houseArea = 2* (houseLength * houseHeight) + 2 * (houseWidth * houseHeight)

totalHouseArea = houseArea - (totalWindowArea + totalDoorArea)

print("The surface area to be painted of a house is ", totalHouseArea, "sqft.")