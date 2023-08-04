from django.test import TestCase
from .models import Contact
# Create your tests here.

class TestContactModel(TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.cls_atomics = cls._enter_atomics()
        cls.data = {
            "name": "Amil",
            "email": "amil@gmail.com",
            "subject": "Subject",
            "message": "Sayt ishlemir!"
        }

        Contact.objects.create(**cls.data)

    def test_creation(self):
        contact_obj = Contact.objects.first()

        self.assertEqual(self.data["name"], contact_obj.name)

    def test_str_method(self):
        contact_obj = Contact.objects.first()
        self.assertEqual(str(contact_obj), self.data["name"])

    @classmethod
    def tearDownClass(cls) -> None:
        Contact.objects.first().delete()
        del cls.data


