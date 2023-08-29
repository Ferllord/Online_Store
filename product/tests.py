from django.test import TestCase
from http import HTTPStatus
from django.urls import reverse

from product.models import Product, ProductCategory


# Create your tests here.


class IndexTestCase(TestCase):

    def test_view(self):
        path = reverse('index')
        response = self.client.get(path)

        self.assertEqual(response.status_code,HTTPStatus.OK)
        self.assertEqual(response.context_data['title'],'Store')
        self.assertTemplateUsed(response, 'product/index.html')

class ProductsListViewTestCase(TestCase):

    fixtures = ['category.json', 'goods.json']

    def setUp(self):
        self.product = Product.objects.all()

    def test_list(self):
        path = reverse('products:list')
        response = self.client.get(path)

        self._common_tests(response)
        self.assertEqual(list(response.context_data['object_list']), list(self.product[:3]))

    def test_list_with_category(self):
        category = ProductCategory.objects.last()
        path = reverse('products:category', args=(2,))
        response = self.client.get(path)


        self._common_tests(response)
        self.assertEqual(
            list(response.context_data['object_list']),
            list(self.product.filter(category_id=category.id))
        )

    def _common_tests(self,response):
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertTemplateUsed(response, 'product/products.html')
