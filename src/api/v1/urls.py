from django.urls import path

from api.v1.cart.cart import CartAPI
from api.v1.cart.items import ItemAPI
from api.v1.product.category import ViewCategory, ViewCategoryStructure
from api.v1.product.product import ViewProduct
from api.v1.review.review import CreateNewReview

urlpatterns = [
    path(
        r'categories/structures/',
        ViewCategoryStructure.as_view(),
        name='categories-structures'
    ),
    path(r'categories/', ViewCategory.as_view(), name='categories-list'),
    path(r'products/by/', ViewProduct.as_view(), name='products-article'),
    path(r'reviews/', CreateNewReview.as_view(), name='reviews-create'),
    path(r'carts/items/', ItemAPI.as_view(), name='items'),
    path(r'carts/', CartAPI.as_view(), name='carts'),
]
