from django.shortcuts import render
from django.http import HttpResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from agenda.models import Item
from .serializers import ItemSerializer

# GET function - get all agenda Items
@api_view(['GET'])
def get_data(request):
    if request.method == 'GET':
        items = Item.objects.all()
        serializer = ItemSerializer(items, many=True)
        return Response(serializer.data)

# unused atm
# GET function - get individual agenda Item by pk
@api_view(['GET', 'DELETE'])
def get_item(request, pk):
    try :
        item = Item.objects.get(pk)
    except Item.DoesNotExist:
        return HttpResponse(status=404)
    
    if request.method == 'GET':
        serializer = ItemSerializer(item)
        return Response(serializer.data)

    if request.method == 'DELETE':
        item.delete()
        return Response(status=status.HTTP_404_NOT_FOUND)

# POST function - add new agenda Item to DB
@api_view(['POST'])
def add_item(request):
    if request.method == 'POST':
        serializer = ItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
    return Response(serializer.data)

# TODO
@api_view(['PUT'])
def update_item(request, pk):
    return 0