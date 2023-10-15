cover_price = 27.95
discount = 0.4
shipping_cost_first_copy = 2.0
shipping_cost_additional_copy = 0.95
num_copies = 50

discounted_price = cover_price * (1 - discount)
total_shipping_cost = shipping_cost_first_copy + (num_copies - 1) * shipping_cost_additional_copy
total = discounted_price * num_copies - total_shipping_cost

print(f"The total wholesale cost for {num_copies} copies is ${total:.2f}")