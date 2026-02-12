# display perimeter of a letter-size paper
# display the length of it's diagonal

# import 
from math import sqrt

# declare variable for diameter & perimeter
paperDiameter = ""
paperPerimeter = ""

# declare variable for paper length & width
paperLengthInInches = float("8.5")
paperWidthInInches = float("11")

# formula for determining perimeter
paperPerimeter = (paperLengthInInches * 2) + (paperWidthInInches *2)

# formula for determining diameter
# d = sqrt (l ** 2) + (w ** 2)
paperDiameter = sqrt((paperLengthInInches ** 2) + (paperWidthInInches ** 2))

print("The perimeter is", paperPerimeter, "inches.")
print("The length of the diagonal is", paperDiameter, "inches.")