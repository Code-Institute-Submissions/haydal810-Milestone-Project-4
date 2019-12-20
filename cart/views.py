from django.shortcuts import render, redirect, reverse

# Note that you don't have to pass in a dictionary of cart_contents because that context is available everywhere.

def view_cart(request):
    """A View that renders the cart contents page"""
    return render(request, "cart.html")

# Add to Cart view

def add_to_cart(request, id):
    """Add a quantity of the specified product to the cart"""
    quantity = int(request.POST.get('quantity'))

    cart = request.session.get('cart', {})
    cart[id] = cart.get(id, quantity)

    request.session['cart'] = cart
    return redirect(reverse('view_cart'))

# Adjust the Cart view

def adjust_cart(request, id):
    """
    Adjust the quantity of the specified product to the specified
    amount
    """
    quantity = int(request.POST.get('quantity'))
    cart = request.session.get('cart', {})

    if quantity > 0:
        cart[id] = quantity
    else:
        cart.pop(id)
    
    request.session['cart'] = cart
    return redirect(reverse('view_cart'))

