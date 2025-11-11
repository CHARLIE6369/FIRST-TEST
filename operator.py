amount = 1000
Tax = amount * 0.18
total = amount+Tax
print(total)
if amount > 800:
    discount = total * 0.10
    total -= discount
print (total)

age=18
if age >= 18:
    print("you may can vote")
else:
    print("you cannot able to vote")