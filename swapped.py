# Read a string from the user and print the string with the first and last 
# characters swapped. 
# Assume that the user will enter a string that has more than 2 characters

text = input("Enter a string: ")

swapped = text[-1] + text[1:-1] + text[0]

print(swapped)