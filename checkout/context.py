from django.shortcuts import get_object_or_404
from products.models import Product


def checkout_contents(request):
    """
    Ensures that the checkout is aviable when rendering every page
    """

    checkout = request.session.get('checkout',{})

    checkout_items = [

    ]

    total = 0
    for id in checkout.items():
        product = get_object_or_404(Product, pk=id)
        total += product.current_action_price
        checkout_items.append({'id':id, 'product':product})

    return {'checkout_items': checkout_items, 'total': total}
