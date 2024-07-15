def nth_largest_number(lst, reverse=True):
    sorted_list = sorted(lst, reverse=True)
    return sorted_list[n-1]

A = [5, 2, 1, 7, 4]
n = 3

result = nth_largest_number(A, n)

print(f"The {n}rd largest number is {result}.")




num=int(input("enter the number of elements:"))
l=[]
for i in range(num):
    x=int(input("enter a no."))
    l.append(x)
print(f"the entered list is {l}")
n=int(input("enter the value of n:"))
l.sort()
print(f"the (n)th largest number is {l[num-n]}")

