def cnt_letters_and_digits(string):
    letter_count = 0
    digit_count = 0
    
    for char in string:
        if char.isalpha():
            letter_count += 1
        elif char.isdigit():
            digit_count += 1
    
    return letter_count, digit_count
input_string = input("Enter a sentence: ")
letters, digits = cnt_letters_and_digits(input_string) 
print(f"LETTERS {letters}")
print(f"DIGITS {digits}")
