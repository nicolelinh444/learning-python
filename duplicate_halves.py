# Read a string from the user and print the string with the first half and the
# second half doubled. For example, Java becomes JaJavava and 1234 becomes 
# 12123434. Assume the user enters a string that has an even number of
# characters.

text = input("Enter a string: ")

middle = len(text) // 2

firstHalf = text[:middle]
secondHalf = text[middle:]

result = (firstHalf * 2) + (secondHalf * 2)

print(result)