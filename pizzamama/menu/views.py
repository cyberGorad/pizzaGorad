from django.shortcuts import render
from django.http import HttpResponse
from .models import Pizza


def index(request):
    '''pizzas = Pizza.objects.all()
    pizza_nom_et_prix = [pizza.nom + ":" + str(pizza.prix) + "$" for pizza in pizzas]
    
    pizza_str = ', '.join(pizza_nom_et_prix)
    return HttpResponse('les pizza de tsilavina: '+ pizza_str)'''
    pizzas = Pizza.objects.all()
    return render(request, 'menu/index.html', {'pizzas' : pizzas})
# Create your views here.
