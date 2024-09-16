# catalog/tests.py

from rest_framework.test import APITestCase
from rest_framework import status
from .models import Product

class ProductTests(APITestCase):
    def setUp(self):
        self.product = Product.objects.create(
            name='Test Product',
            description='Test Description',
            price=10.00,
            inventory_count=100,
            category='Test Category'
        )

    def test_get_products(self):
        response = self.client.get('/api/products/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_product(self):
        data = {
            'name': 'New Product',
            'description': 'New Description',
            'price': 20.00,
            'inventory_count': 50,
            'category': 'New Category'
        }
        response = self.client.post('/api/products/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_update_product(self):
        data = {'inventory_count': 200}
        response = self.client.patch(f'/api/products/{self.product.id}/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.product.refresh_from_db()
        self.assertEqual(self.product.inventory_count, 200)
