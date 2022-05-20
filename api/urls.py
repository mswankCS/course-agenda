from django.urls import path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

# URLs for /agenda/
urlpatterns = [
    path('data/', views.get_data),
    path('data/<int:id>', views.item_detail),
]

urlpatterns = format_suffix_patterns(urlpatterns)
