from rest_framework import serializers
from .models import Customer

# Serializer for Customer model
class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['first_name', 'last_name', 'email', 'password', 'phone', 'address', 'kyc_type', 'kyc', ]

class CustomerKycSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'

class ReviewKycSerializer(serializers.Serializer):
    email = serializers.EmailField()
    kyc = serializers.ImageField()

# Serializer for Account model
# class AccountSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Account
#         fields = '__all__'

# # Serializer for Transaction model
# class TransactionSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Transaction
#         fields = '__all__'