from django.shortcuts import render
from django.http import HttpResponse
import random
# Create your views here.
def home(request):
    return render(request, 'generator/home.html')

def password(request):
    thepassword =''
    length =int(request.GET.get('length',12))
    character=list('abcdefghijklmnopqrstuvewxyz')

    if request.GET.get('uppercase'):
        character.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))

    if request.GET.get('numbers'):
        character.extend(list('1234567890'))

    if request.GET.get('special'):
        character.extend(list('!@$%&*'))

    for i in range(length):
        thepassword+=random.choice(character)
    return render(request, 'generator/password.html', {'password':thepassword})

def about(request):
    return render(request,'generator/about.html')
