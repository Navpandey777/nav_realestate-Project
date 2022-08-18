
from ast import keyword


from http.client import HTTPResponse
from multiprocessing import context
from django.shortcuts import get_object_or_404, render
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from .choices import price_choices, state_choices, bedroom_choices

from .models import listing


def index(request):
    listings = listing.objects.order_by('-list_date').filter(is_published=True)
    paginator = Paginator(listings, 6)
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)

    context = {
        'listings': paged_listings
    }

    return render(request, 'listings/listings.html', context)


def listing_1(request, listing_id):
    listing1 = get_object_or_404(listing, pk=listing_id)

    context = {
        'listing': listing1
    }

    return render(request, 'listings/listing.html', context)


def search_1(request):
    queryset_list = listing.objects.order_by('-list_date')
    
    print("request")
    print(request.GET)

    # keywords
    if 'keywords' in request.GET:

        keywords = request.GET['keywords']
        if keywords:
            queryset_list = queryset_list.filter(
                description__icontains=keywords)
    # city
    if 'city' in request.GET:

        city = request.GET['city']
        if city:
            queryset_list = queryset_list.filter(city__iexact=city)
    # state
    if 'state' in request.GET:

        state = request.GET['state']
        if state:
            queryset_list = queryset_list.filter(state__iexact=state)

    # bedroom
    if 'bedrooms' in request.GET:

        bedrooms = request.GET['bedrooms']
        if bedrooms:
            queryset_list = queryset_list.filter(bedroom__lte =bedrooms)
            
    # price
    if 'price' in request.GET:

        prize = request.GET['price']
        if prize:
            queryset_list = queryset_list.filter(prize__lte =prize)
           
           

    context = {
        'state_choices': state_choices,
        'bedroom_choices': bedroom_choices,
        'price_choices': price_choices,
        'listings': queryset_list,
        'values': request.GET

    }
    return render(request, 'listings/search.html', context)
