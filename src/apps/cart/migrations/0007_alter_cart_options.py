# Generated by Django 4.2 on 2023-04-27 04:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0006_alter_cartitem_unique_together'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cart',
            options={'verbose_name': 'корзина', 'verbose_name_plural': 'корзины'},
        ),
    ]