from django.test import TestCase, Client
from .models import Contact
from django.urls import reverse_lazy
from .forms import ContactForm
# Create your tests here.

class ContactViewUnitTest(TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        client = Client()
        cls.url = reverse_lazy("core:contact")
        cls.response = client.get(cls.url)
        cls.fake_data = {
            "name": "Amil",
            "email": "amilgmail.com",
            "subject": "Subject",
            "message": "Sayt ishlemir!"
        }

        cls.response = client.post(cls.url, data=cls.fake_data)

        return super().setUpClass()
    
    def test_url(self):
        self.assertEqual(self.url, '/en/contact/')

    def test_html_content(self):
        self.assertTemplateUsed(self.response, 'contact.html')

    def test_status(self):
        self.assertEqual(self.response.status_code, 200)

    def test_form_instance(self):
        self.assertIsInstance(self.response.context["form"], ContactForm)

    def test_is_valid(self):
        form = self.response.context["form"]
        self.assertFalse(form.is_valid())
    

    @classmethod
    def tearDownClass(cls) -> None:
        return super().tearDownClass()


# class TestContactModel(TestCase):

#     @classmethod
#     def setUpClass(cls) -> None:
#         cls.cls_atomics = cls._enter_atomics()
#         cls.data = {
#             "name": "Amil",
#             "email": "amil@gmail.com",
#             "subject": "Subject",
#             "message": "Sayt ishlemir!"
#         }

#         Contact.objects.create(**cls.data)

#     def test_creation(self):
#         contact_obj = Contact.objects.first()

#         self.assertEqual(self.data["name"], contact_obj.name)

#     def test_str_method(self):
#         contact_obj = Contact.objects.first()
#         self.assertEqual(str(contact_obj), self.data["name"])

#     @classmethod
#     def tearDownClass(cls) -> None:
#         Contact.objects.first().delete()
#         del cls.data






