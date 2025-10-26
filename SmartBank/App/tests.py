from django.test import TestCase
from .models import Customer
# Create your tests here.
class SimpleTest(TestCase):
    def setUp(self):
        # Set up data for the whole TestCase
        customer = Customer.objects.create(first_name="John", last_name="Doe", email="johndoe@gmail.com", password="password123", phone="1234567890", address="123 Main St", kyc_type="Aadhaar")
        customer.save()
    def test_customer_creation(self):
        customer = Customer.objects.get(email="johndoe@gmail.com")
        self.assertEqual(customer.first_name, "John")   
        self.assertEqual(customer.last_name, "Doe")
        self.assertEqual(customer.email, "johndoe@gmail.com")
    
    def test_customer_password_lenght(self):
        customer = Customer.objects.get(email="johndoe@gmail.com")
        self.assertTrue(len(customer.password) >= 8)
