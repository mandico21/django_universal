import pytest
from django.urls import reverse
from rest_framework import status
from rest_framework.status import HTTP_404_NOT_FOUND
from rest_framework.test import APITestCase

from apps.shop.models import Category, CategoryNode, ProductType

ARTICLE_ID = 123


@pytest.mark.django_db
class TestApiProduct(APITestCase):

    def setUp(self) -> None:
        Category.objects.create(id='1', name='Мужская', description='Пусто')
        CategoryNode.objects.create(id=1, category_id=1, parent_id=None)

        ProductType.objects.create(
            article=ARTICLE_ID,
            category_id=1,
            name='Телефон',
            base_price=1000,
        )

    def test_get_product_by_article_not_found(self) -> None:
        url = reverse('products-article', kwargs={'article': 11})
        response = self.client.get(url)
        assert response.status_code == HTTP_404_NOT_FOUND

    def test_get_product_by_article_success(self) -> None:
        url = reverse('products-article', kwargs={'article': ARTICLE_ID})
        response = self.client.get(url)
        assert response.status_code == status.HTTP_200_OK
        assert response.data['result'].get('article') == ARTICLE_ID
        assert response.data['result'].get('discount') == 0
        assert response.data['error'] == []
