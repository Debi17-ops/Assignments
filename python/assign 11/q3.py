def anagram(str1,str2):

    str1 = str1.lower().replace(" ","")
    str2 = str2.lower().replace(" ","")

    if len(str1) != len(str2):
        return False
    
    freq_str1 = {}
    freq_str2 ={}

    for i in str1:
        if i not in freq_str1:
            freq_str1[i] = 1
        else:
            freq_str1[i] += 1
    

    for i in str2:
        if i not in freq_str2:
            freq_str2[i] = 1
        else:
            freq_str2[i] += 1
    
    if freq_str1 == freq_str2:
        return True
    return False

# taking user input and printing the results
str1 = input("Enter the first string: ")
str2 = input("Enter the second string: ")
if anagram(str1,str2):
    print(f"{str1} and {str2} are anagrams")
else:
    print(f"{str1} and {str2} are not anagrams")