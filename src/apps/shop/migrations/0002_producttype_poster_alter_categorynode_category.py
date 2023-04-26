# Generated by Django 4.2 on 2023-04-26 09:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='producttype',
            name='poster',
            field=models.ImageField(default=1, upload_to='product/poster', verbose_name='Постер'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='categorynode',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='category_nodes', to='shop.category', verbose_name='Категория'),
        ),
    ]