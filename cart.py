# shoppingcart_module.py
def add_item(cart):
    item = input("Enter the item:")
    quantity = int(input("Enter the quantity"))

    if item in cart:
        cart[item] += quantity

    else:
        cart[item] = quantity

    def remove_item(cart):
        item = input("Enter the item")
        if item in cart:
            quantity = int(input("Enter the quantity to remove:"))
            if quantity >=cart[item]:
                del cart[item]
            else:
                cart[item] -= quantity

def show_cart(cart):
    print("Shopping Cart:")
    for item, quantity in cart.items():
        if quantity > 0:
            print(f"{item}: {quantity}")

def shopping_cart():
    cart={}
    while True:
        action= input("Enter an action (add/remove/show/quit):")
        if action == "add":
            add_item(cart)
        elif action == "remove":
            remove_item(cart)
        elif action =="Show":
            show_cart(cart)
        elif action == "quit":
            break
        else:
            print("invalid action. Please try again.")

    print ("items in the cart:")
    for item, quantity in cart.items():
        if quantity > 0:
            print(f"{item}:{quantity}")


