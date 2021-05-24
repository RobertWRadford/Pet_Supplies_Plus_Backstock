from django.contrib import admin
from .models import stockItem

# Register your models here.
@admin.register(stockItem)
class stockItemAdmin(admin.ModelAdmin):
	list_display = ('__str__','quantity')
	list_filter = ('brand', 'quantity')