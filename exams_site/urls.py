from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('exams.urls')),
    path('accounts/', include('django.contrib.auth.urls')),  # логин/логаут
]