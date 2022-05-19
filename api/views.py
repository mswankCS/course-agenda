from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response

from agenda.models import Item
from .serializers import ItemSerializer

@api_view(['GET'])
def get_data(request):
    if request.method == 'GET':
        items = Item.objects.all()
        serializer = ItemSerializer(items, many=True)
        return Response(serializer.data)

@api_view(['POST'])
def add_item(request):
    if request.method == 'POST':
        serializer = ItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
    return Response(serializer.data)
