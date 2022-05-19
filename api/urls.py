from django.urls import path
from . import views

# URLs for /agenda/
urlpatterns = [
    path('data', views.get_data),
    path('add/', views.add_item),
]
