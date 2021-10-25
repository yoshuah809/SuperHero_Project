from django import forms
from .models import Superhero

class HeroForm(forms.ModelForm):
    class Meta:
        model = Superhero
        # fields = ['name', 'alter_ego','primary_ability', 'secondary_ability','catch_phrase']
        fields = '__all__'