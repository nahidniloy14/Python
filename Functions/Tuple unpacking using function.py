shopping_cart = [("Jar", 10), ("Dress", 30), ("CPU", 89), ("Roblox", 5)]


def shopping(shopping_cart):
    max_price = 0
    costly_item_name = ''
    for item, price in shopping_cart:

        if price > max_price:
            max_price = price
            costly_item_name = item

        else:
            pass
    return max_price, costly_item_name


print(shopping(shopping_cart))

# Tuple Unpacking
product_name, price = shopping(shopping_cart)
print(product_name)
print(price)
