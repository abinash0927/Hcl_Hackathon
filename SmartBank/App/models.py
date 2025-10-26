from django.db import models
from django.core.validators import EmailValidator
from django.core.exceptions import ValidationError
from django.contrib.auth.hashers import make_password
# Create your models here.

# Model for Customer
try:
    class Customer(models.Model):
        kyc_choices = [
            ('Aadhaar', 'Aadhaar'),
            ('PAN', 'PAN'),
            ('Passport', 'Passport'),
            ('Driving License', 'Driving License'),
        ]
        first_name = models.CharField(max_length=100)
        last_name = models.CharField(max_length=100)
        email = models.EmailField(unique=True)
        password = models.CharField(max_length=100,)
        phone = models.CharField(max_length=15)
        address = models.TextField()
        kyc_type = models.CharField(max_length=20, choices=kyc_choices, default='Aadhaar')
        kyc = models.ImageField(upload_to='kyc_documents/')
        kyc_verified = models.BooleanField(default=False)
        def __str__(self):
            return self.first_name + " " + self.last_name
        def save(self, *args, **kwargs):
            if not self.pk:  # Only hash password on creation
                self.password = make_password(self.password)
            super().save(*args, **kwargs)
        
except Exception as e:
    print(f"Error creating Customer model: {e}")



