from django.shortcuts import render
from .models import NippoModel
from .forms import NippoFormClass


def nippoListView(request):
    template_name = "nippo/nippo-list.html"
    ctx = {}
    qs = NippoModel.objects.all()
    ctx["object_list"] = qs
    return render(request, template_name, ctx)


def nippoDetailView(request, pk):
    template_name = "nippo/nippo-detail.html"
    ctx = {}
    q = NippoModel.objects.get(pk=pk)
    ctx["object"] = q
    return render(request, template_name, ctx)


def nippoCreateView(request):
    template_name = "nippo/nippo-form.html"
    if request.POST:
        title = request.POST.get("title")
        content = request.POST.get("content")
        obj = NippoModel(title=title, content=content)
        obj.save()
    return render(request, template_name)
