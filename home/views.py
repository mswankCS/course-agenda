from django.shortcuts import render
from django.http import HttpResponse

from .models import TextLine

def display(request):
    lines = TextLine.objects.all()
    if not lines:
        return HttpResponse("No text to display here.<br>")
    else:
        return HttpResponse(lines[0].text)
