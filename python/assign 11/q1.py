def anagrams(s1, s2):

    if len(s1) != len(s2):
        return False
    
    
    char_count = {}
    
    for char in s1:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    
    
    for char in s2:
        if char in char_count:
            char_count[char] -= 1
            if char_count[char] < 0:
                return False
        else:
            return False
    
    
    return all(count == 0 for count in char_count.values())

s1 = "listen"
s2 = "silent"
print(anagrams(s1, s2))  

s1 = "hello"
s2 = "world"
print(anagrams(s1, s2)) 
