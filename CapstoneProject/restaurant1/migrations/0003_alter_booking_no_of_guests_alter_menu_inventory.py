# Generated by Django 4.2.4 on 2023-08-29 19:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant1', '0002_alter_booking_no_of_guests_alter_menu_inventory'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='No_of_guests',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='menu',
            name='Inventory',
            field=models.PositiveIntegerField(),
        ),
    ]
