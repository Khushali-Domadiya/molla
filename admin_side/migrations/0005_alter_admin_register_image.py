# Generated by Django 5.0.6 on 2024-08-19 16:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_side', '0004_alter_admin_register_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='admin_register',
            name='image',
            field=models.FileField(default='', upload_to='./admin_signup'),
        ),
    ]
