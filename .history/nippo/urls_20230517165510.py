from django.urls import path
from .views import nippoListView, nippoDetailView,nippoCreateView

urlpatterns = [
    path("", nippoListView), #ポイント2
    path("detail/<int:number>/", nippoDetailView)
    path("create/", nippoCreateView)
]