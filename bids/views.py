from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib.auth.models import User
from .models import Bid
from auctions.models import Auction
from django.utils import timezone
from datetime import datetime, timedelta
from django.conf import settings
from django.contrib import messages


def all_bids(request):
    """ Shows logged in users all the bids """
    if request.user.is_authenticated:
        bid = Bid.objects.all()
        end_time_list = []
        """ The winning bidder will have chance to pay """
        for i in bid:
            end_time_list.append(str(i.auction_id.end_time))
        #publishable_key = settings.STRIPE_PUBLISHABLE
        #'key':publishable_key,
        return render(request, "bid.html", {"bid": bid,  'end_time':end_time_list})
    else:
        messages.error(request, "You must be Logged in")
        return redirect(reverse('index'))
    return render(request, "index.html")



    
    


    
        
        
        
    

        
        
    
    
        
        
    