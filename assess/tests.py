from django.test import TestCase, Client
from assess.models import Books, Categories
from django.core.urlresolvers import reverse

# Create your tests here.
class TestAssess(TestCase):
    def setUp(self):

        client = Client()
        self.categories= [
                Categories.objects.create(Category="sports"),
                Categories.objects.create(Category="comics"),
                Categories.objects.create(Category="Novel"),
        ]

        Books.objects.create(title="test1",  category=self.categories[0])
        Books.objects.create(title="test2",  category=self.categories[1])
        Books.objects.create(title="test3",  category=self.categories[2])
        Books.objects.create(title="test4",  category=self.categories[0])


    def test_Books_Model(self):
        data = Books.objects.all()
        self.assertEqual(data.count(),4)

    def test_Books_Model(self):
        data = Books.objects.get(title="test1")
        self.assertIsNot(None,data)
        self.assertEqual(data.title,'test1')

    def test_Categories_Model(self):
        data = Categories.objects.all()
        self.assertIsNot(None,data)

    def test_Index_view(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code,200)
    de test_index_view(self)
