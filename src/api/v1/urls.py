from django.urls import path

from api.v1.product.category import ViewCategory, ViewCategoryStructure
from api.v1.product.product import ViewProduct, ViewProductByCategory, ViewProductByBrand
from api.v1.review.review import CreateNewReview

urlpatterns = [
    path('categories/sctructures', ViewCategoryStructure.as_view()),
    path('categories/', ViewCategory.as_view()),
    path('products/article=<int:article>', ViewProduct.as_view()),
    path('products/categoryId=<int:category_id>', ViewProductByCategory.as_view()),
    path('products/brandId=<int:brand_id>', ViewProductByBrand.as_view()),
    path('reviews/', CreateNewReview.as_view()),
]
