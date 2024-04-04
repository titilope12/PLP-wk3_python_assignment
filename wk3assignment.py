def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        final_price = price - ((discount_percent/100)*price)
    else:
        final_price = price
    print(final_price)

price = eval(input("Enter the original price of an item: "))
discount_percent = eval(input("Enter discount percentage: "))

calculate_discount(price, discount_percent)

