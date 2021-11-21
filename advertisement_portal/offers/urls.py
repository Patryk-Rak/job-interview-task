from django.urls import path, include
from . import views


app_name = 'offers'

urlpatterns = [
    path('', views.offer_list, name='offer_list'),
    path('<slug:category_slug>/', views.offer_list, name='offer_list_by_category'),
    path('<int:id>/<slug:slug>/', views.offer_detail, name='offer_detail'),
    path('api/', include('offers.api.urls', namespace='offers_api')),
]
