from django.shortcuts import render
from django.http import HttpResponse

from models import Item

def index(request):
    agenda_item = Item.objects[0]
    output = agenda_item.item_text + " due " + str(agenda_item.due_month) + "/" + (agenda_item.due_day)
    return HttpResponse(output)