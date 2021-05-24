from django.shortcuts import render, redirect, reverse
from django.conf import settings
from django.views import View, generic
from django.contrib.auth import login, authenticate, logout, tokens
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, forms
from django.contrib.auth.models import User
from .models import stockItem

# Create your views here.
def home_view(request, *args, **kwargs):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect('stock')
        else:
        	return render(request, 'index.html', {'form': form, 'incorrect': True})
    else:
        form = AuthenticationForm()
    return render(request, 'index.html', {'form': form})

def stock_view(request, *args, **kwargs):
	if 'remove' in request.POST:
		stockItem.objects.get(pk=request.POST['item']).delete()
	elif 'edit' in request.POST:
		item = stockItem.objects.get(pk=request.POST['item'])
		item.quantity = request.POST['quantity']
		item.save()
	elif 'new' in request.POST:
		new_item = stockItem.objects.create(brand=request.POST['brand'], product=request.POST['product'], quantity=request.POST['quantity'])
		new_item.save()
	context = {
		'items': stockItem.objects.all(),
	}
	return render(request, 'stock.html', context)