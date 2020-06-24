from django.forms import ModelForm
from clientes.models import Person
from django.contrib.auth.models import User

class UserForm(ModelForm):
     class Meta:
         model = User
         fields = ['first_name', 'email', 'password']


