from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('Task.urls')),   # API routes
    path('', include('Task.urls')), 
]