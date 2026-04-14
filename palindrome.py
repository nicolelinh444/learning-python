# Define the main function here...
def main():
   word = input("Enter a string: ")
   if isPalindrome(word):
      print("That's a palindrome.")
   else:
      print("That isn't a palindrome.")

# Define the function isPalindrome(str) here
def isPalindrome(str):
   return str == str[::-1]

# Call the main function.
main()