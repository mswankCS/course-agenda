from rest_framework.test import APIRequestFactory
from django.contrib.auth.models import AnonymousUser, User
from django.test import RequestFactory, TestCase
from .views import get_data, item_detail

class SimpleTest(TestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
        self.user = User.objects.create_user(username='miles', email='Miles.Swank@entrust.com', password='password')

    def test_get_data(self):
        request = self.factory.post('/agenda/data', {'text':'test_item_0', 'due_date'='10-10-2022'})

        request = self.factory.get('/agenda/data')
        request.user = self.user

        response = get_data(request)
        assert(response.status_code == 200)

    def test_item_detail(self):
        request = self.factory.get('agenda/data/1')

# if __name__ == '__main__':
#     t = SimpleTest()
#     t.setUp()

#     t.test_get_data()