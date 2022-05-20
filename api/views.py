from django.shortcuts import render
from django.http import HttpResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from agenda.models import Item
from .serializers import ItemSerializer

# GET, POST - get all agenda Items, add an agenda Item
@api_view(['GET', 'POST'])
def get_data(request, format=None):
    if request.method == 'GET':
        items = Item.objects.all()
        serializer = ItemSerializer(items, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = ItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
    return Response(serializer.data, status=status.HTTP_201_CREATED)

# GET, PUT, DELETE - get an Item by id, update an Item, delete an Item
@api_view(['GET', 'PUT', 'DELETE'])
def item_detail(request, id, format=None):
    try:
        item = Item.objects.get(pk=id)
    except Item.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ItemSerializer(item)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = ItemSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  
    elif request.method == 'DELETE':
        item.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# OLD
# GET function - get individual agenda Item by pk
# @api_view(['GET', 'DELETE'])
# def get_item(request, pk):
#     try :
#         item = Item.objects.get(pk)
#     except Item.DoesNotExist:
#         return HttpResponse(status=404)
    
#     if request.method == 'GET':
#         serializer = ItemSerializer(item)
#         return Response(serializer.data)

#     if request.method == 'DELETE':
#         item.delete()
#         return Response(status=status.HTTP_404_NOT_FOUND)

# POST function - add new agenda Item to DB
# @api_view(['POST'])
# def add_item(request):
#     if request.method == 'POST':
#         serializer = ItemSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#     return Response(serializer.data)