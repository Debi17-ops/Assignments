import random

# Function to create a list of numbers and display 'k' values from it
def create_list():

    lst = [random.randrange(0,100) for i in range(10)]
    print(lst)

    k = int(input("Enter the value of k: "))
    for i in range(k):
        print(random.choice(lst))


create_list()