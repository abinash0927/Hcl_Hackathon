from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import CustomerListCreateView, CustomerRetrieveUpdateDestroyView,ReviewKycView, updateKyc,CustomerUpdateKycView
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView


urlpatterns = [
    path('customers/', CustomerListCreateView.as_view(), name='customer-list-create'),
    path('customers_update/<str:email>/', CustomerUpdateKycView.as_view(), name='customer-list-create'),
    path('customers/<str:email>/', CustomerRetrieveUpdateDestroyView.as_view(), name='customer-detail'),
    
    path('customers/<str:email>/', CustomerRetrieveUpdateDestroyView.as_view(), name='customer-detail'),
    path('customers/<str:email>/kyc_verified/', updateKyc, name='customer-detail'),
    path('kyc_documents/<str:email>/', ReviewKycView, name='customer-detail'),
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
    # path('/kyc_documents/aadhar.jpg/', ReviewKycView.as_view(), name='customer-detail'),  
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)