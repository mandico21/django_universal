# Generated by Django 4.2 on 2023-04-25 09:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0002_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='coupon',
            old_name='end_data',
            new_name='end_date',
        ),
        migrations.RenameField(
            model_name='giftcoupon',
            old_name='end_data',
            new_name='end_date',
        ),
    ]
