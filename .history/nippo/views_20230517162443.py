from django.shortcuts import render
from random import randint


def nippoListView(request):
    return render(request, "nippo/nippo-list.html")


def nippoDetailView(request, number):
    template_name = "nippo/nippo-detail.html"
    random_int = randint(1, 10)
    ctx = {
        "random_number": random_int,
        "number"
    }
    return render(request, template_name, ctx)
