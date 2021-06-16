from django import forms
from .models import stockItem

brands = stockItem.objects.values_list('brand', flat=True).order_by('brand').distinct()

brand_choices = [(str(i+1), brand) for i, brand in enumerate(brands)]
brand_choices.insert(0, ('0', 'All Brands'))

categories = stockItem.objects.values_list('category', flat=True).order_by('category').distinct()

category_choices = [(str(i+1), category) for i, category in enumerate(categories)]
category_choices.insert(0, ('0', 'All Categories'))

class filterSelect(forms.Form):
    brand = forms.ChoiceField(label='Brand', choices=brand_choices)
    category = forms.ChoiceField(label='Category', choices=category_choices)