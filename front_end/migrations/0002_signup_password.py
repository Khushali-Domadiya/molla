# Generated by Django 5.0.6 on 2024-09-12 12:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('front_end', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='signup',
            name='password',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]