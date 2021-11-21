from django.urls import path
from . import views

app_name = 'offers_api'
urlpatterns = [
    path('offers/', views.OfferListView.as_view(), name='offer_list'),
    path('categories/', views.CategoryListView.as_view(), name='category_list'),
    path('offers/<pk>/', views.OfferDetailView.as_view(), name='offer_detail'),
    path('categories/<pk>/', views.CategoryDetailView.as_view(), name='category_detail'),
]