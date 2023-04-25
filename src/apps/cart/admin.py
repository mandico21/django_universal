from django.contrib import admin

from apps.cart.models import Cart, CartItem, Discount, Coupon, Gift, GiftCoupon


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ('client', 'status',)


@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):
    list_display = ('cart', 'product', 'quantity',)


@admin.register(Discount)
class DiscountAdmin(admin.ModelAdmin):
    list_display = ('name', 'discount_type', 'discount_value', 'is_active')


@admin.register(Coupon)
class CouponAdmin(admin.ModelAdmin):
    list_display = ('name', 'code', 'discount', 'start_date', 'end_date')


@admin.register(Gift)
class GiftAdmin(admin.ModelAdmin):
    list_display = ('name', 'product',)


@admin.register(GiftCoupon)
class GiftCouponAdmin(admin.ModelAdmin):
    list_display = ('gift', 'code', 'start_date', 'end_date', 'is_active',)
