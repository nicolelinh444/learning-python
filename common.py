# Write a program that asks a user to type in two strings and prints

# the words that occur in both strings.
# the words that occur in one string but not the other (both ways).
# Print each of the resulting sets sorted alphabetically.
# File name: common.py
# Hint: use set methods we learned in class.

def main():
    string1 = input("Enter the first string: ")
    string2 = input("Enter the second string: ")

    words1 = string1.lower().split()
    words2 = string2.lower().split()

    set1 = set(words1)
    set2 = set(words2)

    # words in both strings
    both = set1.intersection(set2)

    # words only in string 1
    only_1 = set1 - set2

    # words only in string 2
    only_2 = set2 - set1

    print("The words that are in both strings:")
    for word in sorted(both):
        print(word, end=" ")
    print()

    print("The words in string 1 that are not in string 2:")
    for word in sorted(only_1):
        print(word, end=" ")
    print()

    print("The words in string 2 that are not in string 1:")
    for word in sorted(only_2):
        print(word, end=" ")
    print()

main()