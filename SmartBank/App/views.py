from django.shortcuts import render,HttpResponse,redirect
from django.core.exceptions import ObjectDoesNotExist
from .models import Customer
from .serializers import CustomerSerializer,ReviewKycSerializer,CustomerKycSerializer
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from pathlib import Path
from rest_framework.routers import DefaultRouter
from rest_framework import request
from rest_framework import permissions


# Create your views here.
class IsOwnerOrReadOnly(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True

        # Write permissions are only allowed to the owner of the snippet.
        return obj.email == request.user
#view for Customer Api
try:
    class CustomerListCreateView(ListCreateAPIView):
        queryset = Customer.objects.all()
        serializer_class = CustomerSerializer
        permission_classes = [IsAuthenticated]
except Exception as e:
    print(f"Error creating Customer: {e}")

class CustomerUpdateKycView(RetrieveUpdateDestroyAPIView):
    queryset = Customer.objects.all()    
    serializer_class = CustomerSerializer
    lookup_field = 'email'
    permission_classes = [IsOwnerOrReadOnly, IsAuthenticated]
    


#view for Customer specific Detail Api
class CustomerRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerKycSerializer
    lookup_field = 'email'
    permission_classes = [IsAuthenticated]

    def update(self, request, *args, **kwargs):
        return redirect('kyc_verified/')

def updateKyc(request, email):
    customer = Customer.objects.get(email=email)
    if customer.kyc_verified:
        return HttpResponse("KYC succesfully verified.you will be redirected to login page.")
    else:
        return HttpResponse("KYC not yet verified.Check your documents.")

def ReviewKycView(request, email):

    customer = Customer.objects.get(email=email)
    print(customer.kyc.name)
    print(Path(__file__).resolve().parent.parent)

    return render(template_name='verificaton.html', request=request, context={'customers': customer})
    




