# Generated by Django 2.2 on 2022-10-02 14:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0009_auto_20221002_1016'),
    ]

    operations = [
        migrations.RenameField(
            model_name='item',
            old_name='attrValueList',
            new_name='attrValue',
        ),
        migrations.RemoveField(
            model_name='product',
            name='attrList',
        ),
        migrations.CreateModel(
            name='ProductAttribute',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=255)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.Product')),
            ],
        ),
        migrations.CreateModel(
            name='AttributeValue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=255)),
                ('productAttribute', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.ProductAttribute')),
            ],
        ),
    ]