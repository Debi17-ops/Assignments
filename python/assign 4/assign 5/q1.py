'''numbers = [1, 2, 3, 4, 5]
number_check = 3

if number_check in numbers:
    print(f"{number_check} is in the list.")
else:
    print(f"{number_check} is not in the list.")'''





def check_num(num,list):
    if num in list:
        return True
    else:
        return False
list=[]
n=int(input("enter the size of list:"))
print("enter the elements:")
for x in range(0,n):
    ele=int(input())
    list.append(ele)
num=int(input("enter the number to search:"))
res=check_num(num,list)
if res:
    print("the number is present")
else:
    print("the number is not present")





