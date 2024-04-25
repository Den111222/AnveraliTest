from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('bitrix24/', include('bitrix24_integration.urls')),
    path('user_profiles/', include('user_profiles.urls')),
]
