from django.shortcuts import render, redirect, reverse
from django.conf import settings
from django.views import View, generic
from django.contrib.auth import login, authenticate, logout, tokens
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, forms
from django.contrib.auth.models import User
from .models import stockItem
from .forms import filterSelect, brand_choices, category_choices

# Create your views here.
def home_view(request, *args, **kwargs):
    if request.user.is_active:
        if 'logout' in request.POST:
            logout(request)
            return redirect('home')
        elif 'remove' in request.POST:
            stockItem.objects.get(pk=request.POST['item']).delete()
            return redirect('home')
        elif 'edit' in request.POST:
            item = stockItem.objects.get(pk=request.POST['item'])
            item.quantity = request.POST['quantity']
            item.save()
            return redirect('home')
        elif 'new' in request.POST:
            if 'new_brand' in request.POST and 'product' in request.POST and 'quantity' in request.POST and 'upc' in request.POST:
                try:
                    new_item = stockItem.objects.create(brand=request.POST['new_brand'], product=request.POST['product'], quantity=request.POST['quantity'], upc=request.POST['upc'], category=request.POST['new_category'])
                    new_item.save()
                except:
                    return redirect('home')
            return redirect('home')
        elif request.POST.get('brand') or request.POST.get('category'):
            brand_num, brand = '0', 'All Brands'
            if 'brand' in request.POST:
                for tup in brand_choices:
                    if request.POST['brand'] == tup[0]:
                        brand_num, brand = tup[0], tup[1]
            category_num, category = '0', 'All Categories'
            if 'category' in request.POST:
                for tup in category_choices:
                    if request.POST['category'] == tup[0]:
                        category_num, category = tup[0], tup[1]
            request.session['brandNum'] = brand_num
            request.session['brandFiltered'] = brand
            request.session['categoryNum'] = category_num
            request.session['categoryFiltered'] = category
        brand_num = request.session.get('brandNum', '0')
        brand = request.session.get('brandFiltered', 'All Brands')
        category_num = request.session.get('categoryNum', '0')
        category = request.session.get('categoryFiltered', 'All Categories')
        if brand_num == '0' and category_num == '0':
            items = stockItem.objects.all().order_by('brand', 'product')
        elif brand_num == '0':
            items = stockItem.objects.filter(category=category).order_by('brand', 'product')
        elif category_num == '0':
            items = stockItem.objects.filter(brand=brand).order_by('brand', 'product')
        else:
            items = stockItem.objects.filter(brand=brand, category=category).order_by('brand', 'product')
        return render(request, 'stock.html', {'items': items, 'filterForm': filterSelect(), 'brandFiltered': brand_num, 'categoryFiltered': category_num,})
    else:
        if request.method == 'POST':
            if 'guest' in request.POST:
                login(request, authenticate(request, username='Guest', password='Gu3stpa55'))
                return redirect('home')
            form = AuthenticationForm(request, data=request.POST)
            if form.is_valid():
                login(request, form.get_user())
                return redirect('home')
            else:
                return render(request, 'index.html', {'form': form, 'incorrect': True, 'username': request.POST['username']},)
        else:
            form = AuthenticationForm()
        return render(request, 'index.html', {'form': form})