# Generated by Django 5.1.6 on 2025-03-09 09:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Menus', '0003_rename_menu_category_menuitem_menucategory_id'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='menucategory',
            options={'ordering': ['name'], 'verbose_name': 'Menu Category', 'verbose_name_plural': 'Menu Categories'},
        ),
        migrations.AlterModelOptions(
            name='menuitem',
            options={'ordering': ['name'], 'verbose_name': 'Menu Item', 'verbose_name_plural': 'Menu Items'},
        ),
        migrations.RenameField(
            model_name='menuitem',
            old_name='MenuCategory_id',
            new_name='MenuCategory',
        ),
    ]
