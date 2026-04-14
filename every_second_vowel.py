##
#  Print every second letter in a string.
#  Replace vowels with -
#

text = str(input("Enter a string: "))

result1 = ""
i = 0
while i < len(text):
    result1 = result1 + text[i]
    i = i + 2

print("The string with every second letter printed is: ", result1)

result2 = ""
for ch in text:
    if ch == 'a' or ch == 'e' or ch == 'i' or ch == 'o' or ch == 'u' or \
       ch == 'A' or ch == 'E' or ch == 'I' or ch == 'O' or ch == 'U':
        result2 = result2 + "_"
    else:
        result2 = result2 + ch

print("The string with every vowel replaced with - is: ", result2)
