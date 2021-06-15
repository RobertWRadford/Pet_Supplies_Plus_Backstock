from django.shortcuts import render, redirect, reverse
from django.conf import settings
from django.views import View, generic
from django.contrib.auth import login, authenticate, logout, tokens
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, forms
from django.contrib.auth.models import User
from .models import stockItem

# Create your views here.
def home_view(request, *args, **kwargs):
	if request.user.is_active:
		if 'remove' in request.POST:
			stockItem.objects.get(pk=request.POST['item']).delete()
			return redirect('home')
		elif 'edit' in request.POST:
			item = stockItem.objects.get(pk=request.POST['item'])
			item.quantity = request.POST['quantity']
			item.save()
			return redirect('home')
		elif 'new' in request.POST:
			if len(request.POST['brand']) and len(request.POST['product']) and request.POST['quantity'] and request.POST['upc']:
				try:
					new_item = stockItem.objects.create(brand=request.POST['brand'], product=request.POST['product'], quantity=request.POST['quantity'], upc=request.POST['upc'])
					new_item.save()
				except:
					return redirect('home')
			return redirect('home')
		return render(request, 'stock.html', {'items': stockItem.objects.all().order_by('brand', 'product')})
	else:
	    if request.method == 'POST':
	        form = AuthenticationForm(request, data=request.POST)
	        if form.is_valid():
	            login(request, form.get_user())
	            return render(request, 'stock.html', {'items': stockItem.objects.all().order_by('brand', 'product'),})
	        else:
	        	return render(request, 'index.html', {'form': form, 'incorrect': True, 'username': request.POST['username']},)
	    else:
	        form = AuthenticationForm()
	    return render(request, 'index.html', {'form': form})