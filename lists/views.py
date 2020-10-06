from django.http import HttpResponse
from django.shortcuts import render, redirect
from random import randint
from .models import Item
# Create your views here.
def home_page(request):
    if request.method == 'POST':
        Item.objects.create(text=request.POST['item_text'])
        return redirect('/')

    context = {
        "lucky_number":get_lucky_number(),
        'items': Item.objects.all()
    }
    return render(request, 'home.html', context=context)

def get_lucky_number():
    lucky_number = randint(0,1000)
    return(lucky_number)