# Generated by Django 5.0.6 on 2024-08-30 03:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('admin_side', '0014_alter_sub_category_category_name'),
    ]

    operations = [
        migrations.DeleteModel(
            name='sub_category',
        ),
    ]
