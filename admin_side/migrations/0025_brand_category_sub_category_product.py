# Generated by Django 5.0.6 on 2024-08-31 06:30

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_side', '0024_slide_remove_product_brand_name_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand_name', models.CharField(max_length=200)),
                ('image', models.FileField(default='', upload_to='./brand')),
            ],
        ),
        migrations.CreateModel(
            name='category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=50)),
                ('image', models.FileField(default='', upload_to='./category')),
            ],
        ),
        migrations.CreateModel(
            name='sub_category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subcategory_name', models.CharField(max_length=50)),
                ('image', models.FileField(default='', upload_to='./subcategory')),
                ('category_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='admin_side.category')),
            ],
        ),
        migrations.CreateModel(
            name='product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=400)),
                ('prize', models.CharField(max_length=20)),
                ('image', models.FileField(default='', upload_to='./product')),
                ('for_whom', models.CharField(max_length=20)),
                ('brand_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='admin_side.brand')),
                ('category_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='admin_side.category')),
                ('subcategory_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='admin_side.sub_category')),
            ],
        ),
    ]