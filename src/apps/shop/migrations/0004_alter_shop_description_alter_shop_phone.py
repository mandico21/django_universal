# Generated by Django 4.2 on 2023-04-17 02:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_alter_shop_city'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shop',
            name='description',
            field=models.CharField(blank=True, null=True, verbose_name='описание'),
        ),
        migrations.AlterField(
            model_name='shop',
            name='phone',
            field=models.CharField(blank=True, null=True, verbose_name='номер телефона'),
        ),
    ]
