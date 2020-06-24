from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.views.generic.edit import CreateView
from django.urls import reverse, reverse_lazy

# Create your views here.
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