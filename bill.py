# Write a program that calculates the amount of money that everyone has to 
# pay, including the tip after eating in a luxury restaurant.
# Specifications:
  #- Party of four people
  #- Tip is 15%
  #- The total bill amount is $200
  #- Do not use magic numbers in the formula. Save all the values in variables first.

totalBill = 300.0
tip = totalBill * 0.25
partySize = 4

amountPaid = (totalBill + tip) / 4


print("The bill is $ ", totalBill)
print("The tip is $", tip)
print("Each person has to pay $", amountPaid)