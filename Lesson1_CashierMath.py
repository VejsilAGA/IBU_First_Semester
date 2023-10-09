book_price = 24.95
first_shipping = 3
additional_cost = 0.75
discount = 40/100

base_cost = book_price + first_shipping + additional_cost
discount = base_cost * 0.40
final_cost = base_cost - discount

print("The base price is: ", base_cost)
print("This is the discount value: ", discount)
print("This is the final price: ", final_cost)