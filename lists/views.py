from django.http import HttpResponse
from django.shortcuts import render
from random import randint

# Create your views here.
def home_page(request):
    context = {
        "lucky_number":get_lucky_number()
    }
    return render(request, 'home.html', context=context)

def get_lucky_number():
    lucky_number = randint(0,1000)
    return(lucky_number)