
def duplicate(String):
    list=String.split(',')
    final=[]
    for i in list:
        if i not in final:
            final.append(i)
    return final

user_list=input("enter the comma separated list:")
list=duplicate(user_list)
print(list)
