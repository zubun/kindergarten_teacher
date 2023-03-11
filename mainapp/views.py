from django.shortcuts import render


# Create your views here.
def main(request):
    return render(request, "mainapp/index.html")


def about(request):
    return render(request, "mainapp/about.html")


def blog_single(request):
    return render(request, "mainapp/blog_single.html")


def category(request):
    return render(request, "mainapp/category.html")


def contact(request):
    return render(request, "mainapp/contact.html")


def homepage_2(request):
    return render(request, "mainapp/homepage_2.html")


def index(request):
    return render(request, "mainapp/index.html")


def search(request):
    return render(request, "mainapp/search.html")
