from django.urls import path

from . import views  # Импорт view-функций приложения Blog.

app_name = 'blog'  # Определение пространства имен приложения Blog.
urlpatterns = [
    path('', views.index, name='index'),  # Главная страница проекта.
    path('posts/<int:id>/', views.post_detail, name='post_detail'),  # Развернутая страница поста.
    path('category/<slug:category_slug>/', views.category_posts, name='category_posts'),  # Страница категорий поста.
]
