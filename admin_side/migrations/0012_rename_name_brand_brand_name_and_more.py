# Generated by Django 5.0.6 on 2024-08-30 03:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('admin_side', '0011_sub_category'),
    ]

    operations = [
        migrations.RenameField(
            model_name='brand',
            old_name='name',
            new_name='brand_name',
        ),
        migrations.RenameField(
            model_name='category',
            old_name='name',
            new_name='category_name',
        ),
    ]