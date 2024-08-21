from django.urls import path
from .views import ItemListCreate

urlpatterns = [
    path('api/data/', ItemListCreate.as_view(), name='item-list-create'),
]
