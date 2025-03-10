# Generated by Django 5.1.6 on 2025-03-09 04:32

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MenuCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=75, unique=True)),
                ('descriptions', models.TextField(max_length=200)),
                ('order_count', models.IntegerField(default=0)),
                ('is_active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='MenuItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=75, unique=True)),
                ('image', models.ImageField(upload_to=None)),
                ('descriptions', models.TextField(max_length=200)),
                ('order_count', models.IntegerField(default=0)),
                ('is_active', models.BooleanField(default=True)),
                ('created_at', models.DateField(auto_now_add=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=5)),
                ('is_available', models.BooleanField(default=True)),
                ('menu_category_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Menus.menucategory')),
            ],
        ),
    ]
