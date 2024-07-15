def substring(sub_str, main_str):
    
    len_sub = len(sub_str)
    len_main = len(main_str)
    
    
    for i in range(len_main - len_sub + 1):
        if main_str[i:i + len_sub] == sub_str:                         
            return True
    return False


main_string = input("Enter the main string : ")
sub_string = input("Enter the substring : ")


if substring(sub_string, main_string):
    print(f"'{sub_string}' is in the main string.")
else:
    print(f"'{sub_string}' is not in the main string.")
