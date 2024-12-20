def matchwords(words):
    counter = 0
    w =[]
    for word in words:
        if len(word) > 1 and word[0] == word[-1]:
            counter = counter + 1
            w.append(word)
        
    print("List of words with first and last character matching\n", w)
    return counter


inputvalue = input("Enter the words separated by spaces: ")
words = inputvalue.split()
count = matchwords(words)
print("Number of words with first and last character matching", count)