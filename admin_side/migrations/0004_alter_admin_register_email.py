# Generated by Django 5.0.6 on 2024-08-19 16:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_side', '0003_rename_admin_sign_admin_register'),
    ]

    operations = [
        migrations.AlterField(
            model_name='admin_register',
            name='email',
            field=models.EmailField(max_length=100),
        ),
    ]
