# Generated by Django 4.1.2 on 2023-03-12 16:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pos_close_control', '0005_employee_is_used'),
    ]

    operations = [
        migrations.AddField(
            model_name='possession',
            name='odoo_version',
            field=models.IntegerField(default=15),
        ),
    ]
