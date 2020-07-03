from django.urls import path
from .views import new_user, perfil
from .views import CreateUser, RegisterUser

urlpatterns = [
   path('new_user', new_user, name="new_user"),
   path('accounts/', CreateUser.as_view(), name='accounts'),
   path('register/', RegisterUser.as_view(), name='register'),
   path('perfil', perfil, name="perfil"),
]
