from django.urls import path

from . import views  # Импорт view-функций приложения Pages.

app_name = 'pages'  # Определение пространства имен приложения Pages.
urlpatterns = [
    path('pages/about/', views.about, name='about'),  # Страница о проекте.
    path('pages/rules/', views.rules, name='rules'),  # Страница правил.
]
