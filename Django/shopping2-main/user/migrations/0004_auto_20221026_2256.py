# Generated by Django 2.2 on 2022-10-26 15:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_myuser_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myuser',
            name='email',
            field=models.CharField(default='', max_length=255, null=True, unique=True),
        ),
    ]