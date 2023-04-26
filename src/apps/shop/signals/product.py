from django.core.cache import cache
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from apps.shop.models import ProductType, CategoryNode, Category


@receiver(post_save, sender=ProductType)
@receiver(post_delete, sender=ProductType)
def clear_product_cache(sender: ProductType, instance: ProductType, **kwargs):
    cache_key_product = f'product_type:article={instance.pk}'
    cache_key_category = f'category_node_product_types:category_id={instance.category_id}'
    cache_key_brand = f'brand_product_types:brand_id={instance.brand_id}'
    cache.delete(cache_key_product)
    cache.delete(cache_key_category)
    cache.delete(cache_key_brand)


@receiver([post_save, post_delete], sender=CategoryNode)
def clear_category_node_cache(sender: CategoryNode, instance: CategoryNode, **kwargs):
    for product in instance.product_types.all():
        cache_key_product = f'product_type:article={product.article}'
        cache.delete(cache_key_product)
    cache_key_category = f'category_node_product_types:category_id={instance.category_id}'
    cache.delete(cache_key_category)


@receiver([post_save, post_delete], sender=Category)
def clear_category_cache(sender: Category, instance: Category, **kwargs):
    for category_node in instance.category_nodes.all():
        cache_key_category = f'category_node_product_types:category_id={category_node.id}'
        cache.delete(cache_key_category)
        for product_type in category_node.all():
            cache_key_product = f'product_type:article={product_type.article}'
            cache.delete(cache_key_product)
