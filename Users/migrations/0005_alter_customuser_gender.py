# Generated by Django 5.1.6 on 2025-03-05 18:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0004_customuser_gender_alter_customuser_phone_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='gender',
            field=models.TextField(blank=True, max_length=50, null=True),
        ),
    ]
