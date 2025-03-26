from django.shortcuts import render


def index(request):
    return render(request, 'blog/index.html')


def post_detail():
    return None


def category_post():
    return None
