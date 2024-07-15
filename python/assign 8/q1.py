products = [ 
    {'name': 'orange', 'price': 20}, 
    {'name': 'apple', 'price': 8}, 
    {'name': 'banana', 'price': 10}, 
    {'name': 'kiwi', 'price': 30} 
]

for i in products:
    if i['price'] > 10:
        print(i['name'])
