from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Superhero
from django.urls import reverse


# Create your views here.
def index(request):
    all_heroes = Superhero.objects.all()
    contex = {
        'all_heroes': all_heroes
        }
    return render(request, 'superheroes/index.html', contex)

def create(request):
    if request.method == 'POST':
        #Save content in new database
        # Return to index page
        name = request.POST.get('name')
        alter_ego = request.POST.get('alter_ego')
        primary = request.POST.get('primary')
        secondary = request.POST.get('secondary')
        catchphrase = request.POST.get('catch_phrase')
        new_hero = Superhero(name=name, 
                                alter_ego=alter_ego, 
                                primary_ability=primary, 
                                secondary_ability=secondary, 
                                catch_phrase=catchphrase)
        new_hero.save()
        return HttpResponseRedirect(reverse('superheroes:index'))

        # return render(request, 'superheroes/create.html')  