# Generated by Django 2.2 on 2022-09-30 11:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0005_auto_20220930_1749'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='description',
            field=models.TextField(default='', null=True),
        ),
    ]
