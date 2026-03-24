from django.urls import path

from . import views

app_name = "reminders"

urlpatterns = [
    path("", views.index, name="index"),
    path("lists/<int:pk>/", views.view_list, name="view_list"),
    path("lists/add/", views.add_list, name="add_list"),
]
