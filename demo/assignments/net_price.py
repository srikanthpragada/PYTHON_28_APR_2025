# Take price and display net price
price = float(input("Enter price :"))

if price > 1000:
    discount = price * 0.20
elif price > 500:
    discount = price * 0.15
elif price > 200:
    discount = price * 0.10
else:
    discount = price * 0.05

net_price = price - discount

print(f"Price        : {price:5.0f}")
print(f"- Discount   : {discount:5.0f}")
print(f"Net Price    : {net_price:5.0f}")
