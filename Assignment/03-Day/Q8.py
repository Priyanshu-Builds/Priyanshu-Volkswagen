qty = int(input("Enter the quantity you want to buy: "))
unit_price = 5
total_price = qty * unit_price

if qty > 50:
    discount = 0.15
elif qty > 30:
    discount = 0.10
else:
    discount = 0

final_price = total_price - (total_price * discount)

print("Total price before discount is:", total_price)
print("Discount applied is:", discount * 100, "%")
print("Amount you need to pay is:", final_price)