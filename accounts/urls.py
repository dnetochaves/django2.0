from django.urls import path
from .views import new_user, perfil
from .views import CreateUser

urlpatterns = [
   path('new_user', new_user, name="new_user"),
   path('accounts/', CreateUser.as_view(), name='accounts'),
   path('perfil', perfil, name="perfil"),
]
