from django.shortcuts import render, get_object_or_404
from .models import Offer, Category


def offer_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    offers = Offer.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        offers = offers.filter(category=category)
    return render(request,
                  'offers/list.html',
                  {'category': category,
                   'categories': categories,
                   'offers': offers})

def offer_detail(request, id, slug):
    offer = get_object_or_404(Offer,
                                id=id,
                                slug=slug,
                                available=True)
    return render(request, 'offers/detail.html', {'offer': offer})