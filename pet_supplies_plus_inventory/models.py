from django.db import models

# Create your models here.
class stockItem(models.Model):
	brand = models.CharField(max_length=25, help_text='Enter the brand name of the item.')
	product = models.CharField(max_length=75, help_text='Enter the item description.', unique=True)
	quantity = models.IntegerField()

	def __str__(self):
		return f'{self.brand}: {self.product}'