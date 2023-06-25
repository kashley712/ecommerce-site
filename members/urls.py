from django.urls import path
from . import views
from django.contrib import admin


urlpatterns = [
    path('members/', views.members, name='members'),
]
#
#urlpatterns = [
    #path('index/', views.indexpage, name='indexpage'),
   # path('shopitem/', views.shopitempage, name='shopitempage'),


from django.urls import path
from . import views

urlpatterns = [
    path('members/', views.members, name='members'),  # Add this line
    path('index/', views.indexpage, name='indexpage'),  # Existing URL pattern for 'indexpage'
    path('shopitem/', views.shopitempage, name='shopitempage'),  # Existing URL pattern for 'shopitempage'
    # Rest of the URL patterns
    
]
