from django.shortcuts import render
from django.http import HttpResponse
from .forms import Userforms

# Create your views here.

def registeruser(request):
    form = Userforms
    context = {
        form: 'form',
    }

    return render (request , 'account/registrationform.html', context)
