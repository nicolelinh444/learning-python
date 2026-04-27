#
#  Read a word from the user, and display its characters in reverse order.
#

# str makes the input a string
word = str(input("Enter a word: "))

# initializes empty string
reversed = ""

# len(word) is like word.length in JS
# subtract 1 because indexing starts at 0
i = len(word) - 1

# while loop
while i >= 0:
    # concatenate the string with +
    reversed = reversed + word[i]

    # decrement i
    i = i - 1

# print is like console.log()
# commas add spaces between values
print(word, "reversed is ", reversed)
