from django.contrib import admin
from django.urls import path, include

#swagger URL
from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title='POLICYQUOTE APIs')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('apps.accounts.urls')),
    path('api-auth/', include('rest_framework.urls'))
]

