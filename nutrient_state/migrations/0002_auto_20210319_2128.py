# Generated by Django 3.1.7 on 2021-03-19 21:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nutrient_state', '0001_add_nutrients_column'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='lettucenutrients',
            table='nutrientes_alface',
        ),
    ]