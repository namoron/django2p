from django.urls import path
from .views import nippoListView #ポイント1
from .views import nippoDetailView #ポイント1

urlpatterns = [
    path("", nippoListView), #ポイント2
    path("", nippoDetailView), #ポイント2
]