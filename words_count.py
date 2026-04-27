# Write a program that counts how often each word occurs in the following string:


# “It was the best of times, it was the worst of times, it was the age of wisdom, it was the age of foolishness, it was the epoch of belief, it was the epoch of incredulity, it was the season of Light, it was the season of Darkness, it was the spring of hope, it was the winter of despair"

# As the program goes through the words, it should save the word and the frequency of the word as a pair in a dictionary. Then, print the words with the count of each word sorted alphabetically. 

# File name: words_count.py

# Hint: use split() function to convert the string into a list of words.
# “It” and “it” are the same word. You should ignore capitalization 

def main():
   str = "It was the best of times, it was the worst of times, it was the age of wisdom, it was the age of foolishness, it was the epoch of belief, it was the epoch of incredulity, it was the season of Light, it was the season of Darkness, it was the spring of hope, it was the winter of despair"

    # make text lowercase
    str = str.lower()

    words = str.split()

    word_count = {}

    for word in words:
       word_count[word] = word_count.get(word, 0) + 1

    for word in sorted(word_count):
        print(word + ":", word_count[word])

main()