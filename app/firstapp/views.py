from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.http import HttpResponseNotFound
from .models import Person

# Create your views here.

def index(request):
    people = Person.objects.all()
    return render(request,'firstapp/index.html',{'people':people})

def create(request):
    if request.method == 'POST':
        pers = Person()
        pers.name = request.POST.get('name')
        pers.surname = request.POST.get('surname')
        pers.age = request.POST.get('age')
        pers.save()
    return HttpResponseRedirect('/')

def edit(request,id):
    try:
        person = Person.objects.get(id = id)
        if request.method == 'POST':
            person.name = request.POST.get('name'),
            person.surname = request.POST.get('surname')
            person.age = request.POST.get('age')
            person.save()
            return HttpResponseRedirect('/')
        else:
            return render(request,'firstapp/edit.html',{'person':person})
    except Person.DoesNotExist:
        return  HttpResponseNotFound("<h2>Person not found</h2>")

def delete(request,id):
    try:
        person = Person.objects.get(id=id)
        person.delete()
        return HttpResponseRedirect('/')
    except Person.DoesNotExist:
        return HttpResponseNotFound("<h2>Person not found</h2>")