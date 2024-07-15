

items = [(60,10),(100,20),(120,30)]
# given input , weight = 50
Wt = 50
total_value = 0
total_weight = 0

# using list comprehension , created a list containing ratios , value and weight
ratio = [ (items[i][0] / items[i][1], items[i][0], items[i][1]) for i in range(len(items ))]

ratio.sort(reverse = True)

print(ratio)

for ratio,value,weight in ratio:


    if total_weight + weight <= Wt:
        total_value += value
        total_weight += weight
    else:
        remaining_weight = (Wt - total_weight ) / weight
        total_value += value * remaining_weight
        break

# prinitng the total value for the input , Wt = 50
print(total_value)

