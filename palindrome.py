# Define the main function here...
def main():
   word = input("Enter a string: ")

   # calling the helper function
   if isPalindrome(word):
      print("That's a palindrome.")
   else:
      print("That isn't a palindrome.")

## helper function
# Define the function isPalindrome(str) here
# "str" is the parameter name 

def isPalindrome(str):
   # sequence[start : stop : step]
   # python slice method - start/stop is empty so we use the whole string
   # -1 means go backwards
   return str == str[::-1]

# Call the main function.
main()