from django.urls import path
from .views import list_clientes, new

urlpatterns = [
   path('list_clientes', list_clientes, name="list_clientes"),
   path('new', new, name="new"),
]
