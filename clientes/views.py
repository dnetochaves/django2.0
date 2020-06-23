from django.shortcuts import render, redirect
from .models import Person
from .forms import PersonForm

# Create your views here.
def list_clientes(request):
    persons = Person.objects.all()
    return render(request, 'clientes/list_clientes.html', {'persons': persons})

def new(request):
    form = PersonForm(request.POST, request.FILES, None)

    if form.is_valid():
        form.save()
        return redirect('list_clientes')
    return render(request, 'clientes/person_form.html', {'form': form})
