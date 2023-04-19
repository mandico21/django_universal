from django.urls import path

from api.v1.product.category import ViewCategory, ViewCategoryStructure
from api.v1.product.product import ViewProduct, ViewProductByCategory, ViewProductByBrand
from api.v1.review.review import CreateNewReview

urlpatterns = [
    path(r'categories/sctructures', ViewCategoryStructure.as_view(), name='categories-sctructures'),
    path(r'categories/', ViewCategory.as_view(), name='categories-list'),
    path(r'products/article=<int:article>', ViewProduct.as_view(), name='products-article'),
    path(r'products/categoryId=<int:category_id>', ViewProductByCategory.as_view(), name='products-category'),
    path(r'products/brandId=<int:brand_id>', ViewProductByBrand.as_view(), name='products-brand'),
    path(r'reviews/', CreateNewReview.as_view(), name='reviews-create'),
]
