from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from blog.models import Post, Category
from django.contrib.auth.models import User


# Create your tests here.

class PostTest(APITestCase):

    def test_view_posts(self):
        url = reverse('blog_api:listcreate')  # get ulr for list create po nazwie w tym przypadkiu /api/
        response = self.client.get(url, format='json')  # get response from url
        self.assertEqual(response.status_code, status.HTTP_200_OK)  # test if return status is 200 ok

    def create_post(self):
        test_category = Category.objects.create(name="django")  # tworzenie kategorii django
        testuser1 = User.objects.create_user(
            username='test_user1', password='123456789'
        )

        data = {'title': "new", "author": 1,
                "excerpt": "new", "content": "new"}
        url = reverse('blog_api:listcreate')
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
