product_quantities = [13, 5, 6, 10, 11] 
prices = [1.2, 6.5, 1.0, 4.8, 5.0]

total_price =[product_quantities[i] * prices[i] for i in range(len(prices))]

print(total_price)
print(sum(total_price))