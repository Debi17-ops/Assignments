def find_consonant(string):
    vowel_list=['a','e','i','o','u','A','E','I','O','U']

    count=0
    for x in string:
        if x.isalpha():
            if x not in vowel_list:
                count+=1
    return count

sample=input("enter the string:")
res=find_consonant(sample)
print(f"the number of consonants in the string is{res}")
