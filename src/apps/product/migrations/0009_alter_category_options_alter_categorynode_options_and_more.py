# Generated by Django 4.2 on 2023-04-17 06:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0008_alter_producttype_description_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'Категория', 'verbose_name_plural': 'Категории'},
        ),
        migrations.AlterModelOptions(
            name='categorynode',
            options={'verbose_name': 'Подкатегория', 'verbose_name_plural': 'Подкатегории'},
        ),
        migrations.AlterField(
            model_name='category',
            name='description',
            field=models.CharField(blank=True, max_length=120, null=True, verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='category',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False, verbose_name='ID категории'),
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=64, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='categorynode',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.category', verbose_name='Категория'),
        ),
        migrations.AlterField(
            model_name='categorynode',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False, verbose_name='ID подкатегории'),
        ),
        migrations.AlterField(
            model_name='categorynode',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='childrens', to='product.categorynode', verbose_name='ID подкатегории'),
        ),
    ]
