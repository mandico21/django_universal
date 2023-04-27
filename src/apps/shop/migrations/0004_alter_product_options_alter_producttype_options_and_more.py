# Generated by Django 4.2 on 2023-04-27 04:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_alter_attribute_description_alter_attribute_name_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'verbose_name': 'Товар на складе', 'verbose_name_plural': 'Товары на складах'},
        ),
        migrations.AlterModelOptions(
            name='producttype',
            options={'verbose_name': 'Товар', 'verbose_name_plural': 'Товары'},
        ),
        migrations.AlterField(
            model_name='product',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='shop.producttype', verbose_name='Товар'),
        ),
    ]
