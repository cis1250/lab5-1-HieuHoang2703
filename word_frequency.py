#!/usr/bin/env python3

# Word frequency exercise
# TODO: (Read detailed instructions in the Readme file)

import re

#Global variable
end_punctuations = ['.', '?', '!']
punctuations = ['(',')',',','.','!','?',"'",'"', ':', ';']

#Get sentence function
def get_sentence()
    sentence = input("Enter a sentence")
    while (not sentence[0].isupper()) or (sentence[-1] not in end_punctuations) or (len(sentence.strip()) == 0):
        sentence = input("Please enter a valid sentence")
    return sentence
    
#Calculate frequency function
def calculate_frequencies(sentence):
    for char in punctuations:
        sentence = sentence.replace(char, "")
    #Split the sentence
    split_words = sentence.split()
    #Initialize word_list and frequency 
    word_list = []
    frequency = []
    #Loop
    for word in split_words:
        word = word.lower()
        if word in word_list:
            frequency_index = word_list.index(word)
            frequency_index[frequency_index] += 1
        else:
            word_list.append(word)
            frequency.append(1)
    return word_list, frequency

#Print function
def print_frequencies(words, frequencies):
    print("Frequencies of Words is:")
    for i in range(len(words)):
        print(f"{words[i]}: {frequencies[i]}")

#Main function
def main():
    sentence = get_sentence()
    words, frequencies = calculate_frequencies(sentence)
    print_frequencies(words, frequencies)

#Run the program
main()


#This is a function that checks if a text qualifies as a sentence. You do not need to modify this!
def is_sentence(text):
    # Check if the text is not empty and is a string
    if not isinstance(text, str) or not text.strip():
        return False

    # Check for starting with a capital letter
    if not text[0].isupper():
        return False

    # Check for ending punctuation
    if not re.search(r'[.!?]$', text):
        return False

    # Check if it contains at least one word (non-whitespace characters)
    if not re.search(r'\w+', text):
        return False

    return True
