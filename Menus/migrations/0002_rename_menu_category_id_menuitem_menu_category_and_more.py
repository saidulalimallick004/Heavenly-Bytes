# Generated by Django 5.1.6 on 2025-03-09 04:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Menus', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='menuitem',
            old_name='menu_category_id',
            new_name='menu_category',
        ),
        migrations.AlterField(
            model_name='menuitem',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
    ]
