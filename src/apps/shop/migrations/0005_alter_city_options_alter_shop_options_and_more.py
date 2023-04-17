# Generated by Django 4.2 on 2023-04-17 06:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_alter_shop_description_alter_shop_phone'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='city',
            options={'verbose_name': 'Город', 'verbose_name_plural': 'Города'},
        ),
        migrations.AlterModelOptions(
            name='shop',
            options={'verbose_name': 'Магазин', 'verbose_name_plural': 'Магазины'},
        ),
        migrations.AlterField(
            model_name='city',
            name='code',
            field=models.CharField(verbose_name='Код города'),
        ),
        migrations.AlterField(
            model_name='city',
            name='name',
            field=models.CharField(verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='shop',
            name='address',
            field=models.CharField(verbose_name='Адрес магазина'),
        ),
        migrations.AlterField(
            model_name='shop',
            name='city',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='shops', to='shop.city', verbose_name='Город'),
        ),
        migrations.AlterField(
            model_name='shop',
            name='description',
            field=models.CharField(blank=True, null=True, verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='shop',
            name='name',
            field=models.CharField(verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='shop',
            name='phone',
            field=models.CharField(blank=True, null=True, verbose_name='Номер телефона'),
        ),
    ]
