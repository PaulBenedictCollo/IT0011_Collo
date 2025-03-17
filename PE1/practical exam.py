def word_counter():
    # get input from user
    text_input = input("Enter a string statement:\n")
    
    # list of words to ignore
    ignore_list = ['a', 'an', 'the', 'and', 'but', 'or', 'nor', 'for', 'so', 'yet', 'of']
    
    # remove commas and periods, splits the sentence into words
    word_list = text_input.replace(',', '').replace('.', '').split()
    
    # create a list of valid words that are not in the ignore list
    valid_words = []
    for word in word_list:
        if word.lower() not in ignore_list:
            valid_words.append(word)
    
    # count the occurrences of each word
    freq = {}
    for word in valid_words:
        if word in freq:
            freq[word] += 1  # increase the count
        else:
            freq[word] = 1   # set count to 1
    
    # separate words into two groups: lowercase and capitalized
    lower_words = []
    upper_words = []
    for word in freq.keys():
        if word.islower():
            lower_words.append(word)
        else:
            upper_words.append(word)
    
    # sort both lists alphabetically
    lower_words.sort()
    upper_words.sort()
    
    # print word counts lowercase words first capitalized words second
    for word in lower_words + upper_words:
        print(word.ljust(10), "-", freq[word])
    
    # print total number of valid words filtered
    print("Total Words Filtered:", len(valid_words))

# call the function
word_counter()
