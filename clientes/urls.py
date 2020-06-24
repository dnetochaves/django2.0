from django.urls import path
from .views import list_clientes, new, update, delete

urlpatterns = [
   path('list_clientes', list_clientes, name="list_clientes"),
   path('new', new, name="new"),
   path('update/<int:id>/', update, name="update"),
   path('delete/<int:id>/', delete, name="delete"),
]
