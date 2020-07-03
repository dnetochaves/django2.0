from django.shortcuts import render, redirect, get_object_or_404
from .models import Person
from .forms import PersonForm
from django.contrib.auth.decorators import login_required
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.urls import reverse, reverse_lazy
    
# Create your views here.
#CBV
class PersonList(ListView):
    model = Person          

class PersonDetailView(DetailView):
    model = Person

class PersonCreate(CreateView):
    model = Person
    fields = ['first_name', 'last_name','age', 'salary', 'bio', 'photo', 'doc']
    success_url = reverse_lazy('person_list')


#FBV
@login_required
def list_clientes(request):
    nome = request.GET.get('nome', None)
    sobrenome = request.GET.get('sobrenome', None)
    if nome:
        persons = Person.objects.filter(first_name__icontains=nome) | Person.objects.filter(last_name__icontains=sobrenome)
        return render(request, 'clientes/list_clientes.html', {'persons': persons})
    else:
         persons = Person.objects.all()
         return render(request, 'clientes/list_clientes.html', {'persons': persons})
   

    

@login_required
def new(request):
    form = PersonForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        form.save()
        return redirect('list_clientes')
    return render(request, 'clientes/person_form_fbv.html', {'form': form})


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

