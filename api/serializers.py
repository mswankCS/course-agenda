from rest_framework import serializers
from agenda.models import Item

# Serializer for Item object
class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'

