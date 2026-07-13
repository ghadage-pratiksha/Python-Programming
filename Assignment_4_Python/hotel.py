def calculate_bill(amount):
    if amount < 500:
        return amount
    elif amount <= 1500:
        return amount - (amount * 0.10)
    else:
        return amount - (amount * 0.15)

amount = int(input("Enter Bill Amount: "))
result = calculate_bill(amount)
print("Bill After Discount =", int(result))
