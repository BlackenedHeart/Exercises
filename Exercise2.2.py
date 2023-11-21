word1 = input("Enter the first word: ")
word2 = input("Enter the second word: ")

if word1 < word2:
    print(word1, "comes before", word2)
else:
    print(word2, "comes before", word1)

# Using ternary operator
result = (word1, word2) if word1 < word2 else (word2, word1)
print(result[0], "comes before", result[1])