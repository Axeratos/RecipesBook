from django.shortcuts import render


def index(request):
    return render(request, "recipes_book/index.html")
