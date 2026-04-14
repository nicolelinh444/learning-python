##
#  Sell a limited number of cinema tickets.
#

tickets = 40
buyers = 0

print("There are currently ", tickets, "tickets remaining.")

while tickets > 0:
   num = int(input("How many tickets would you like to purchase? "))
    
   if num < 1 or num > 10:
      print("Sorry, you can't buy that many.")
   elif num > tickets:
      print("Sorry, you can't buy that many.")
   else:
      tickets = tickets - num
      buyers = buyers + 1
      
      if tickets > 0:
         print("There are currently", tickets, "tickets remaining.")

print("The total number of buyers was ", buyers)
