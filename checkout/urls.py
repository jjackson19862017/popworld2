from django.conf.urls import url
from .views import view_checkout

urlpatterns = [
    
    url(r'^$', view_checkout, name='view_checkout'),
    
       
    ]