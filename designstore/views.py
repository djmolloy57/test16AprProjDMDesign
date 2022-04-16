from django.shortcuts import render
from . import forms

# Create your views here.
def designstore(request):
    context = {}
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