from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader

# Create your views here.
def home(request):
    data = {
        'prenom' : 'charlene',
        'montres' : ['tissot','mondaine','seiko'],
        'age' : 17
    }
    template = loader.get_template('index.html')
    return HttpResponse(template.render(data))
