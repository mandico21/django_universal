from django.urls import path

from api.v1.product.category import ViewCategory, ViewCategoryStructure
from api.v1.product.product import ViewProduct, ViewProductByCategory

urlpatterns = [
    path('categories/sctructures', ViewCategoryStructure.as_view()),
    path('categories/', ViewCategory.as_view()),
    path('products/article=<int:article>', ViewProduct.as_view()),
    path('products/categoryId=<int:category_id>', ViewProductByCategory.as_view()),
]

# router = routers.SimpleRouter()
# router.register(r'products', ViewProduct2, basename='products')
# urlpatterns = router.urls
