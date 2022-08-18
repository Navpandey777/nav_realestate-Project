from django.contrib import admin 
from django.urls import path
from.import views


urlpatterns = [
    path('',views.index,name='listings'),
  
    path('<int:listing_id>',views.listing_1,name='listing'),
    
    path('search' ,views.search_1,name='search'),

]

    
    