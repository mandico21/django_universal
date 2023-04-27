from django.contrib import admin

from apps.cart.models import Cart, CartItem, Discount, Coupon, Gift, GiftCoupon
from apps.common.admin import CacheAdminMixin


class CartItemInline(admin.TabularInline):
    model = CartItem
    extra = 0
    classes = ['collapse']


@admin.register(Cart)
class CartAdmin(CacheAdminMixin):
    list_display = ('client', 'status',)
    inlines = [CartItemInline]
    readonly_fields = ('total_amount', 'created_at', 'updated_at',)


@admin.register(CartItem)
class CartItemAdmin(CacheAdminMixin):
    list_display = ('cart', 'product', 'quantity',)


@admin.register(Discount)
class DiscountAdmin(CacheAdminMixin):
    list_display = ('name', 'discount_type', 'discount_value', 'is_active')


@admin.register(Coupon)
class CouponAdmin(CacheAdminMixin):
    list_display = ('name', 'code', 'discount', 'start_date', 'end_date')


@admin.register(Gift)
class GiftAdmin(CacheAdminMixin):
    list_display = ('name', 'product',)


@admin.register(GiftCoupon)
class GiftCouponAdmin(CacheAdminMixin):
    list_display = ('gift', 'code', 'start_date', 'end_date', 'is_active',)
