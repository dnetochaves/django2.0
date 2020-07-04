from django.urls import path
from .views import list_clientes, new, update, delete
from .views import PersonList, PersonDetailView, PersonCreate, PersonUpdate, PersonDelete

urlpatterns = [

   #FBV
   path('list_clientes', list_clientes, name="list_clientes"),
   path('new', new, name="new"),
   path('update/<int:id>/', update, name="update"),
   path('delete/<int:id>/', delete, name="delete"),

   #CBV
   path('person-list', PersonList.as_view(), name="person-list"),
   path('person_detail/<int:pk>/', PersonDetailView.as_view(), name='person-detail'),
   path('person-create', PersonCreate.as_view(), name="person-create"),
   path('person-update/<int:pk>/', PersonUpdate.as_view(), name='person-update'),
   path('person-delete/<int:pk>/', PersonDelete.as_view(), name='person-delete'),
]
