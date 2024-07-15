import random

def dice():
    return (random.randint(1,6))

# empty dictionary to store occurences of numbers 1-6
count_freq = {i:0 for i in range(1,7)}

# loop to roll a dice 500 times
for i in range(500):
    c = dice()
    count_freq[c] += 1

for num,count in count_freq.items():

    print(f"num {num} appeared {count} times")
