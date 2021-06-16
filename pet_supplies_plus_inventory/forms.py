from django import forms
from .models import stockItem

brands = stockItem.objects.values_list('brand', flat=True).order_by('brand').distinct()

brand_choices = [(str(i+1), brand) for i, brand in enumerate(brands)]
brand_choices.insert(0, ('0', 'All Brands'))

class brandSelect(forms.Form):
    brand = forms.ChoiceField(label='Filter by brand:', choices=brand_choices)