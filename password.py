# Define the main function here...

def main():
   while True:
      password = input("Enter your password: ")
      confirm = input("Re-enter your password: ")
      
      if password != confirm:
         print("That password didn't have the required properties.")
         continue
   
      if isValidPassword(password):
         print("That pair of passwords will work.")
         break
      else:
         print("That password didn't have the required properties.")

# Define the function isValidPassword(password) here...
def isValidPassword(password):
   if len(password) < 8:
      return False
   
   has_upper = False
   has_lower = False
   has_digit = False
   has_special = False
   special_ch = "#@&"
   
   for ch in password:
      if ch.isupper():
         has_upper = True
      elif ch.islower():
         has_lower = True
      elif ch.isdigit():
         has_digit = True
      elif ch in special_ch:
         has_special = True
         
   return has_upper and has_lower and has_digit and has_special

# Call the main function.
main()