from django.shortcuts import render, redirect


def landing_page(request):
    return render(request, "index.html")


def test(request):
    return render(request, "test.html")