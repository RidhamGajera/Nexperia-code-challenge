from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/users/', include('users.urls')),
]

urlpatterns += [
    path('api/campaigns/', include('campaigns.urls')),
]
