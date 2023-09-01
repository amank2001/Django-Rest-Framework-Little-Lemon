from rest_framework import serializers
from .models import Menu
from .models import Booking

class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = ['ID', 'Title', 'Price', 'Inventory']
        extra_kwargs = {
            'Price': {'min_value': 2},
            'Inventory': {'min_value': 0}
        }
        
class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'