with open('assign 14\sowpods.txt','r') as fp:
    lines=fp.readlines()
    words_list=[]
    for line in lines:
        word=line.strip()
        if 'UU' in word:
            words_list.append(word)
    print(words_list)