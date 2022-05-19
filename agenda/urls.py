from django.urls import path
from . import views

# Currently unused
urlpatterns = [
    path('', views.index, name = 'index'),
]