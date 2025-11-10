amount = 1000
Tax = amount * 0.18
total = amount+Tax
print(total)
if amount > 800:
    discount = total * 0.10
    total -= discount
print (total)
