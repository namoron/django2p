from django.shortcuts import render
from random import randint


def nippoDetailView(request):
    template_name = "nippo/nippo-detail.html"
    random_int = randint(1, 10)
    ctx = {
        "random_number": random_int,
    }
    return render(request, template_name, ctx)
