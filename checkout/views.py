from django.shortcuts import render, reverse, redirect
from django.utils import timezone
from auctions.models import Auction
from bids.models import Bid
from django.contrib import messages
from django.conf import settings  


def view_checkout(request):
    """ Checkout Page"""
    return render(request, "checkout.html")




    