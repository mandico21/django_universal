# Generated by Django 4.2 on 2023-04-25 12:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
        ('cart', '0004_alter_coupon_description_alter_discount_description_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Дата последнего обновления')),
                ('status', models.CharField(choices=[('new', 'Новая'), ('active', 'Активная'), ('ordered', 'Оформленная'), ('cancelled', 'Отмененная'), ('refunded', 'Возврат'), ('completed', 'Завершенная')], default='new', verbose_name='Статус')),
                ('total_amount', models.IntegerField(verbose_name='Итоговая сумма')),
                ('amount', models.IntegerField(verbose_name='Сумма скидки')),
                ('cart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cart.cart', verbose_name='Корзина')),
                ('coupon', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cart.coupon', verbose_name='Купон')),
                ('discount', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cart.discount', verbose_name='Скидка')),
                ('gift_coupon', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cart.giftcoupon', verbose_name='Купон подарка')),
            ],
            options={
                'verbose_name': 'Заказ',
                'verbose_name_plural': 'Заказы',
            },
        ),
        migrations.CreateModel(
            name='OrderDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Дата последнего обновления')),
                ('price', models.IntegerField(verbose_name='Цена')),
                ('quantity', models.IntegerField(verbose_name='Количество')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cart.order', verbose_name='Заказ')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.product', verbose_name='Товар')),
            ],
            options={
                'verbose_name': 'Деталь заказа',
                'verbose_name_plural': 'Детали заказа',
            },
        ),
    ]