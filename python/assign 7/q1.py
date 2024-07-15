def common_prefix(str1, str2):
    min_len = min(len(str1), len(str2))
    for i in range(min_len):
        if str1[i] != str2[i]:
            return str1[:i]
    return str1[:min_len]

str1 = input("Enter the first string: ")
str2 = input("Enter the second string: ")

prefix = common_prefix(str1, str2)
print(f"The longest common prefix is: '{prefix}'")
