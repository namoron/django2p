from django.shortcuts import render
from .models import NippoModel

def nippoListView(request):
    return render(request, "nippo/nippo-list.html")


def nippoDetailView(request, number):
    template_name = "nippo/nippo-detail.html"
    random_int = randint(1, 10)
    ctx = {
        "random_number": random_int,
        "number": number,
    }
    return render(request, template_name, ctx)

def nippoCreateView(request):
    template_name="nippo/nippo-form.html"

    if request.POST:
        title = request.POST["title"]
        content = request.POST["content"]

    #受け取った値で必要な処理を行います
        
    return render(request, template_name)


def nippoListView(request):
    template_name = "nippo/nippo-list.html"
    ctx = {}
    qs = NippoModel.objects.all()
    ctx["object_list"] = qs

    return render(request, template_name, ctx)