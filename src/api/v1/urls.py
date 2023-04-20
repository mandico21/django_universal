from django.urls import path

from api.v1.cart.cart import CartAPI
from api.v1.cart.items import ItemAPI
from api.v1.product.category import ViewCategory, ViewCategoryStructure
from api.v1.product.product import ViewProduct, ViewProductByCategory, ViewProductByBrand
from api.v1.review.review import CreateNewReview

urlpatterns = [
    path(r'categories/sctructures/', ViewCategoryStructure.as_view(), name='categories-sctructures'),
    path(r'categories/', ViewCategory.as_view(), name='categories-list'),
    path(r'products/article=<int:article>', ViewProduct.as_view(), name='products-article'),
    path(r'products/categoryId=<int:category_id>', ViewProductByCategory.as_view(), name='products-category'),
    path(r'products/brandId=<int:brand_id>', ViewProductByBrand.as_view(), name='products-brand'),
    path(r'reviews/', CreateNewReview.as_view(), name='reviews-create'),
    # path(r'products/add/cartId=<uuid:cart_id>&product_id=<int:product_id>&quantity=<int:quantity>',
    #      AddProductToCart.as_view(), name='add-product'),
    path(r'carts/items/', ItemAPI.as_view(), name='items'),
    path(r'carts', CartAPI.as_view(), name='carts'),
    # path(r'carts/<uuid:client_id>', CartAPI.as_view(), name='carts-get'),
]
