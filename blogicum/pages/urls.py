from django.urls import path

from . import views  # Импорт view-функций приложения Pages.

app_name = 'pages'  # Определение пространства имен приложения Pages.
urlpatterns = [
    path('about/', views.about, name='about'),  # Страница о проекте.
    path('rules/', views.rules, name='rules'),  # Страница правил.
]
