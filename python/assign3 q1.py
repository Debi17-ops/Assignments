def cnt_alphabets(string):
    alphabet_count = 0
    for char in string:
        if char.isalpha():
            alphabet_count += 1
    
    return alphabet_count
input_string = input("Enter a string: ")
alphabet_count = cnt_alphabets(input_string)
print(f"The number of alphabets in the string is: {alphabet_count}")





def cnt(input_string):
    sum=0
    for x in input_string:
        if('a'<=x<='z') or ('A'<=x<='z'):
            sum=sum+1
    return sum
input_string=input("enter any string:")
alphabet=cnt("input_string")
if alphabet==0:
    print("there are no alphabets")
else:
    print(f"the given string has:{alphabet} alphabtes")



