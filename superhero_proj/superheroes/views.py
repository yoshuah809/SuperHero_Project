from django.http import HttpResponse, HttpResponseRedirect, HttpRequest
from django.shortcuts import render
from django.urls import reverse
from django.template.loader import get_template

from .forms import HeroForm

from .models import Superhero



# Create your views here.
# Create your views here.

# def index(self):
#     template = get_template('superheroes.index.html')
#     return HttpResponse(template.render())


def index(request):
    hero = HeroForm()
    return render(request, 'superheroes/create.html', {"form": hero})

def process_form(request):
    hero = HeroForm(request.POST)
    if hero.is_valid():
        hero.save()
        form = HeroForm()
    return render(request, 'superheroes/display.html', {"form": form, "message": 'OK'})   

def list_heroes(request):
    heroes = Superhero.objects.all()    
    return render(request, 'superheroes/display.html', {"heroes": heroes})
    

def create(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        alter_ego = request.POST.get('alter_ego')
        primary = request.POST.get('primary')
        secondary = request.POST.get('secondary')
        catchphrase = request.POST.get('catch_phrase')
        hero = Superhero(name=name, 
                                alter_ego=alter_ego, 
                                primary_ability=primary, 
                                secondary_ability=secondary, 
                                catch_phrase=catchphrase)
        hero.save()

         # Return to index page
      
        return HttpResponseRedirect(reverse('superheroes:index'))
    else:
        return render(request, 'superheroes/create.html')  

def edit(request, id):
    hero = Superhero.objects.get(pk=id)
    form = HeroForm(instance=hero)
    return render(request,'superheroes/edit.html', {"form":form, "hero":hero}) 

def show(request, id):
    hero = Superhero.objects.get(pk=id)
    form = HeroForm(instance=hero)
    return render(request,'superheroes/showhero.html', {"form":form, "hero":hero})     

def update(request, id):
    hero = Superhero.objects.get(pk=id)
    form = HeroForm(request.POST, instance=hero)  
    if form.is_valid():
        form.save()  
    heroes = Superhero.objects.all()
    return render(request, 'superheroes/display.html', {"heroes": heroes})

def form(self):
    template = get_template('superheroes/form.html')
    return HttpResponse(template.render())
   

def delete (request,id):
    hero = Superhero.objects.get(pk=id)
    hero.delete()
    heroes = Superhero.objects.all()
    return render(request, 'superheroes/display.html', {"heroes": heroes, "message": 'OK'})


