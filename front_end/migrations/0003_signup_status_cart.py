# Generated by Django 5.0.6 on 2024-09-13 03:50

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_side', '0026_remove_category_image'),
        ('front_end', '0002_signup_password'),
    ]

    operations = [
        migrations.AddField(
            model_name='signup',
            name='status',
            field=models.IntegerField(default=1),
        ),
        migrations.CreateModel(
            name='cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.BigIntegerField()),
                ('prize', models.BigIntegerField()),
                ('sub_total', models.BigIntegerField()),
                ('product_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='admin_side.product')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='front_end.signup')),
            ],
        ),
    ]