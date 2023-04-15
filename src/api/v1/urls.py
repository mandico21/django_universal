from django.urls import path

from api.v1.product.category import ViewCategory, ViewCategoryStructure

urlpatterns = [
    path('categories/sctructures', ViewCategoryStructure.as_view()),
    path('categories/', ViewCategory.as_view()),
]

# router = routers.SimpleRouter()
# router.register(r'categories/sctructures/', CategoryNodeView, basename='category')
# router.register(r'categories/', CategoryNodeView, basename='category')
# urlpatterns = router.urls
