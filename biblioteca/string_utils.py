#accepts a pipe separated string and returns a list
def deserialize(cart):
    if(cart is not None):
        cart_list = cart.split("|")
    else:
        cart_list = []
    return cart_list

#accepts a list and returns a pipe separated string
def serialize(cart):
    serialized_cart = '|'.join(cart)
    return serialized_cart