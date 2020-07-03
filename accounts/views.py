from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.views.generic.edit import CreateView
from django.urls import reverse, reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.views import generic

# Create your views here.

def perfil(request):
    return render(request, 'accounts/perfil.html')


def new_user(request):
    form = User(request.POST, request.FILES, None)
    return render(request, 'accounts/user_form.html', {'form': form})



class CreateUser(CreateView):
    model = User
    template_name = 'accounts/user_form.html'
    success_url = reverse_lazy('website')

    fields = [
        'first_name',
        'last_name',
        'username',
        'email',
        'password',
    ]


class RegisterUser(generic.CreateView):
        form_class = UserCreationForm
        success_url = reverse_lazy('login')
        template_name = 'accounts/register.html'
    