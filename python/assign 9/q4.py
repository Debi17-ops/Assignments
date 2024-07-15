def dictionary(sentence):
    list_of_words=sentence.split()
    word_length_dict={word:len(word) for word in list_of_words}
    return word_length_dict

string=input("enter the senetence:")

word_length=dictionary(string)
print(word_length)