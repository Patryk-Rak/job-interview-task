from ..models import Offer, Category
from rest_framework import serializers

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name',
                  'ordering', 'slug']


class OfferSerializer(serializers.ModelSerializer):
    modules = CategorySerializer(many=True, read_only=True)
    class Meta:
        model = Offer
        fields = ['id', 'category',
                  'title', 'description',
                  'slug', 'image',
                  'price', 'available',
                  'created', 'updated', 'modules']