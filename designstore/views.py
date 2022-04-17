from django.shortcuts import render, redirect, get_object_or_404
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

def edit_item(request, item_id):
    item = get_object_or_404(TestItems, id=item_id) #get instance of TestItems model with an id equal to the id passed into the view via url
    form = ItemForm(request.POST, instance=item)
    if form.is_valid():
        form.save()
        return redirect('designstore')
 
    form = ItemForm(instance=item)
    context = {
        'form' : form 
    }
    return render(request, 'designstore/edit_item.html', context)


def toggle_item(request, item_id):
    item = get_object_or_404(TestItems, id=item_id)
    item.done = not item.done 
    item.save() 
    return redirect('designstore')

def delete_item(request, item_id):
    item = get_object_or_404(TestItems, id=item_id)
    item.delete() 
    return redirect('designstore')

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