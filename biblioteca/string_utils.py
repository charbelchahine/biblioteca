#accepts a pipe separated string and returns a list
def deserialize(cart):
    cart_list = cart.split("|")
    return cart_list

#accepts a list and returns a pipe separated string
def serialize(cart):
    serialized_cart = '|'.join(cart)
    return serialized_cart