from django.shortcuts import render, redirect, get_object_or_404
from .models import Person
from .forms import PersonForm
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def list_clientes(request):
    persons = Person.objects.all()
    return render(request, 'clientes/list_clientes.html', {'persons': persons})

@login_required
def new(request):
    form = PersonForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        form.save()
        return redirect('list_clientes')
    return render(request, 'clientes/person_form.html', {'form': form})


@login_required
def update(request, id):
    person = get_object_or_404(Person, pk=id)
    form = PersonForm(request.POST or None, request.FILES or None, instance=person)

    if form.is_valid():
        form.save()
        return redirect('list_clientes')
    return render(request, 'clientes/person_form.html', {'form': form})

@login_required
def delete(request, id):
    person = get_object_or_404(Person, pk=id)

    if request.method == 'POST':
        person.delete()
        return redirect('list_clientes')

    return render(request, 'clientes/person_delete_confirm.html', {'person': person})

