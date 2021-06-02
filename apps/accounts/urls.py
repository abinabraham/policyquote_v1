from django.urls import path, include
from . import views 
from rest_framework import routers 

#custom URLS
from apps.policy import views as p_views

router = routers.DefaultRouter()
router.register('api/v1/policy/age_band', p_views.AgeBandviewSet)
router.register('api/v1/policy/type', p_views.PolicyTypeviewSet)


router.register('api/v1/create_customer', views.UserViewSet)
router.register('api/v1/policy/details', p_views.PolicyViewSet)

router.register('api/v1/policy/quote', p_views.QuoteViewSet)


urlpatterns = [
    path('', include(router.urls))
]