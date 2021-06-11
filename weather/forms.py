from django.db import models
from django.forms import ModelForm,TextInput, fields, widgets
from .models import City

class CityForm(ModelForm):
    class Meta:
        model=City
        fields='__all__'
        widgets={'name': TextInput(attrs={'class':'form-control me-2','placholder':'Search'})}