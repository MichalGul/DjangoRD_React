from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from blog.models import Post, Category
from django.contrib.auth.models import User
from rest_framework.test import APIClient


# Create your tests here.

class PostTest(APITestCase):

    def test_view_posts(self):
        url = reverse('blog_api:listcreate')  # get ulr for list create po nazwie w tym przypadkiu /api/
        response = self.client.get(url, format='json')  # get response from url
        self.assertEqual(response.status_code, status.HTTP_200_OK)  # test if return status is 200 ok

    # def create_post(self):
    #     test_category = Category.objects.create(name="django")  # tworzenie kategorii django
    #     testuser1 = User.objects.create_user(
    #         username='test_user1', password='123456789'
    #     )
    #
    #     data = {'title': "new", "author": 1,
    #             "excerpt": "new", "content": "new"}
    #     url = reverse('blog_api:listcreate')
    #     response = self.client.post(url, data, format='json')
    #     self.assertEqual(response.status_code, status.HTTP_201_CREATED)

#### DOES NOT WORK FOR ME :( ####
    def test_post_update(self):

        client = APIClient()

        test_category = Category.objects.create(name='django')
        testuser1 = User.objects.create_user(
            username='test_user1', password='123456789'
        )
        # self.testuser2 = User.objects.create_user(
        #     username='test_user2', password='123456789'
        # )
        testuser1.save()
        test_post = Post.objects.create(
            category_id=test_category.id, title='Post Title', excerpt='Post Excerpt', content='Post Content', slug='post-title', author_id=2, status='published')
        test_post.save()
        client.login(username=testuser1.username,
                     password='123456789')

        url = reverse(('blog_api:detailcreate'), kwargs={'pk': 1})

        response = client.put( # data to put to api
            url, {
                "title": "New",
                "author": 1,
                "excerpt": "New",
                "content": "New",
                "status": "published"
            }, format='json')
        print(response.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)