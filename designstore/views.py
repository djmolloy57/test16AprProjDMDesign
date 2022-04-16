from django.shortcuts import render, redirect
from . import forms

from .models import TestItems
from .forms import ItemForm

# Create your views here.

def add_item(request):
    if request.method == "POST":
        #name = request.POST.get('item_name') //old method
        #done = 'done' in request.POST //old method
        # TestItems.objects.create(name=name, done=done) //old method

        form = ItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('designstore')

    form = ItemForm()
    context = {
        'form' : form 
    }
    return render(request, 'designstore/add_item.html',context)


def designstore(request):

    items = TestItems.objects.all()
    context = {
        'items' : items
    }
    #context = {}
    return render(request, 'designstore/designstore.html',context)

def cart(request):
    context = {}
    return render(request, 'designstore/cart.html', context)

def checkout(request):

    context = {}
    return render(request, 'designstore/checkout.html', context)

def viewitem(request):
    context = {}
    return render(request, 'designstore/viewitem.html', context)


#look at 7min 27 seconds https://www.youtube.com/watch?v=G-Rct7Na0UQ

def form_name_view(request):
    form = forms.FormName()

    if request.method == 'POST':
        form = forms.FormName(request.POST)

        if form.is_valid():
            #Do something code
            print("VALIDATION SUCCESS!")
            print("NAME: " +form.cleaned_data['name'])
            print("EMAIL: "+form.cleaned_data['email'])
            print("TEXT: "+form.cleaned_data['text'])

    return render(request, 'designstore/form_page.html',{'form': form})