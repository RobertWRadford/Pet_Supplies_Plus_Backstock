# Generated by Django 3.2.3 on 2021-06-15 01:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pet_supplies_plus_inventory', '0002_alter_stockitem_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='stockitem',
            name='upc',
            field=models.CharField(max_length=12, null=True, unique=True),
        ),
    ]
