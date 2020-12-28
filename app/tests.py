from rest_framework.test import APITestCase, APIClient
from django.test import TestCase

from .models import Category


create_json = {
    "name": "Category 1",
    "children": [
        {
            "name": "Category 1.1",
            "children": [
                {
                    "name": "Category 1.1.1",
                    "children": [
                        {
                            "name": "Category 1.1.1.1"
                        },
                        {
                            "name": "Category 1.1.1.2"
                        },
                        {
                            "name": "Category 1.1.1.3"
                        }
                    ]
                },
                {
                    "name": "Category 1.1.2",
                    "children": [
                        {
                            "name": "Category 1.1.2.1"
                        },
                        {
                            "name": "Category 1.1.2.2"
                        },
                        {
                            "name": "Category 1.1.2.3"
                        }
                    ]
                }
            ]
        }
    ]
}


class CategoryTest(TestCase):
    """ Test module for Category model """
    def setUp(self):
        parent = Category.objects.create(
            name='Category 2')
        Category.objects.create(
            name='Category 2.1', parent=parent)

    def test_Category_breed(self):
        category_second = Category.objects.get(name='Category 2.1')
        parent = Category.objects.get(id=category_second.parent.id)
        self.assertEqual(
            category_second.name, "Category 2.1")
        self.assertEqual(
            parent.name, "Category 2")


class RequestsTests(APITestCase):

    def test_categories(self):
        client = APIClient()

        response = client.post('/category/', create_json, format='json')
        self.assertEqual(response.status_code, 201)
        category = Category.objects.get(name='Category 1.1')
        self.assertTrue(category)
        response = client.get('/category/{}/'.format(category.id), format='json')
        self.assertEqual(response.status_code, 200)
