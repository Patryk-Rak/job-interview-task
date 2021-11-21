from django.contrib import admin
from .models import Offer, Category


@admin.register(Offer)
class OfferAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'price',
                    'available', 'created', 'updated']
    list_filter = ['available', 'created', 'updated']
    list_editable = ['price', 'available']
    prepopulated_fields = {'slug': ('title',)}


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'ordering', 'slug']
    prepopulated_fields = {'slug': ('name',)}
