from rest_framework import serializers
from .models import MenuItem

class MenuItemSeralizer(serializers.ModelSerializer):
    class Meta:
        model = MenuItem
        fields = ['title', 'price', 'inventory'] 

