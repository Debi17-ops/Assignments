'''def discounted_price(original_price, discount_percent):
    discount_amount = (original_price * discount_percent) / 100.0
    
    
    discounted_price = original_price - discount_amount
    
    return discounted_price

original_price = 100.0
discount_percent = 20
discounted_price = discounted_price(original_price, discount_percent)
print(f"Original Price: ${original_price}")
print(f"Discount Percent: {discount_percent}%")
print(f"Discounted Price: ${discounted_price:.2f}")'''




def discounted_price(original_price, discount_percent):
    discount_amount = (original_price * discount_percent) / 100.0
    
    
    discounted_price = original_price - discount_amount
    
    return discounted_price


original_price = float(input("Enter the original price of the product: "))
discount_percent = int(input("Enter the discount percentage: "))


calc_discounted_price = discounted_price(original_price, discount_percent)

# Print the result
print(f"Original Price: ${original_price}")
print(f"Discount Percent: {discount_percent}%")
print(f"Discounted Price: ${calc_discounted_price:.2f}")

