from django.shortcuts import render, reverse, redirect, get_object_or_404
from django.utils import timezone
from auctions.models import Auction
from bids.models import Bid
from django.contrib import messages
from django.conf import settings  
from django.contrib.auth.decorators import login_required
from .forms import MakePaymentForm, OrderForm
from .models import OrderLineItem
from products.models import Product
import stripe

stripe_api_key = settings.STRIPE_SECRET

def view_checkout(request):
    """ Checkout Page"""
    return render(request, "checkout.html")

@login_required
def checkout(request):
    if request.method=="POST":
        order_form = OrderForm(request.POST)
        payment_form = MakePaymentForm(request.POST)

        if order_form.is_valid() and payment_form.is_valid():
            order = order_form.save(commit=False)
            order.date = timezone.now()
            order.save
        
            cart = request.session.get('checkout',{})
            total = 0
            for id in cart.items():
                product = get_object_or_404(Product, pk=id)
                total = product.current_auction_price
                order_line_item = OrderLineItem(
                    order = order,
                    product = product
                    )
                order_line_item.save()

            try:
                customer = stripe.Charge.create(
                    amount = int(total * 100),
                    currency = "GBP",
                    description = request.user.email,
                    card = payment_form.cleaned_data['stripe_id'],
                )
            except stripe.error.CardError:
                messages.error(request, "Your card was declined!")

            if customer.paid:
                messages.error(request, "You have successfully paid")
                request.session['cart'] = {}
                return redirect(reverse('products'))
            else:
                messages.error(request, "Unable to take payment")
        else:
            print(payment_form.errors)
            messages.error(request, "We were unable to take a payment with that card!")
    else:
        payment_form = MakePaymentForm()
        order_form = OrderForm()

    return render(request, "checkout.html", {'order_form': order_form, 'payment_form': payment_form, 'publishable':settings.STRIPE_PUBLISHABLE})