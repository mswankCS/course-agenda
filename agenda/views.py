from django.shortcuts import render
from django.http import HttpResponse

from .models import Item

def index(request):
    items = Item.objects.all()
    if not items:
        return HttpResponse("No agenda items to display here.<br>")
    else:
        output = "=== Listing Agenda Items ===<br>"
        for i,item in enumerate(items):
            output += str(i + 1) + ") " + item.item_text + " due " + str(item.item_due_month) + "/" + str(item.item_due_day) + "<br>"
        return HttpResponse(output)