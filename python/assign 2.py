def concatenate(str1, str2):
    return str1 + " " + str2
string1 = input("Enter the first string: ")
string2 = input("Enter the second string: ")
result = concatenate(string1, string2)
print("Concatenated string:", result)


def charprint(strr,index):
    if(index>len(strr)-1):
        print("invalid input\n")
    else:
         print(strr[index])
my_string = str(input("Enter a string: "))
index = int(input("Enter an index: "))
charprint("string,index")


my_string = input("Enter a string: ")
reversed_string = my_string[::-1]
print("Reversed string:", reversed_string)





my_string = input("Enter a string: ")
start_index = int(input("Enter the start index: "))
end_index = int(input("Enter the end index:"))
string = my_string[start_index:end_index]
print("Substring between indices", start_index, "and", end_index, ":",string)

