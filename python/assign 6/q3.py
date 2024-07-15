def word_frequency(sentence):

    words = sentence.split()

    frequency = {}
    for word in words:
        if word in frequency:
            frequency[word] += 1
        else:
            frequency[word] = 1
    return frequency

sentence = input("Enter a sentence: ")
frequency = word_frequency(sentence)
print("Word frequency:", frequency)
