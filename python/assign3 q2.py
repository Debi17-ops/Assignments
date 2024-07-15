def cmp_strings(str1, str2):
    len1 = len(str1)
    len2 = len(str2)
    
    if len1 > len2:
        print(f"The string with the maximum length is: {str1}")
    elif len2 > len1:
        print(f"The string with the maximum length is: {str2}")
    else:
        print("Both strings have the same length:")
        print(str1)
        print(str2)
str1 = input("Enter the first string: ")
str2 = input("Enter the second string: ")
cmp_strings(str1, str2)
