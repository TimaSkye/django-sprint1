from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),  # Подключение маршрутов из приложения Blog.
    path('pages/', include('pages.urls')),  # Подключение маршрутов из приложения Pages.
]
