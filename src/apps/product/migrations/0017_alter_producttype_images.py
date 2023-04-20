# Generated by Django 4.2 on 2023-04-20 04:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('imageledger', '0001_initial'),
        ('product', '0016_alter_producttype_images'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producttype',
            name='images',
            field=models.ManyToManyField(blank=True, related_name='product_images', to='imageledger.imageledger'),
        ),
    ]
