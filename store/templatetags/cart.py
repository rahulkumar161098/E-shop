from django import template

register = template.Library()

@register.filter(name='in_cart')
def is_in_cart(product_id, cart):
    key= cart.keys()
    for id in key:
        if int(id) == product_id.id:
            return True
    # print(product_id, cart)
    return False
    

@register.filter(name='quantity')
def qunatity(product_id, cart):
    key= cart.keys()
    for id in key:
        if int(id) == product_id.id:
            return cart.get(id)
    # print(product_id, cart)
    return 0
    


@register.filter(name='total')
def total_price(product_id, cart):
    return product_id.price * qunatity(product_id, cart)



@register.filter(name="total_cart_price")
def cart_total_price(product_id, cart):
    sum=0
    for p in product_id:
        print(p)
        sum= sum+total_price(p, cart)
    return sum


@register.filter(name="rupee_symbol")
def currency(number):
    return "₹ "+ str(number)

