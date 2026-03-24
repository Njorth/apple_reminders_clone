from django.db.models import Count
from django.http import HttpRequest
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from django.views.decorators.http import require_POST

from reminders.forms import AddListForm

from .models import List


def index(request: HttpRequest):
    context = {
        "lists": List.objects.annotate(reminder_count=Count("reminders")),
        "is_editing": "edit" in request.GET,
    }
    return render(request, "reminders/index.html", context)


def view_list(request: HttpRequest, pk: int):
    lst = get_object_or_404(List.objects.prefetch_related("reminders"), pk=pk)
    context = {
        "list": lst,
        "reminders": lst.reminders.all(),
    }
    return render(request, "reminders/view_list.html", context)


def add_list(request: HttpRequest):
    form = AddListForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect("reminders:index")

    context = {
        "form": form,
    }
    return render(request, "reminders/add_list.html", context)


@require_POST
def delete_list(request: HttpRequest, pk: int):
    lst = get_object_or_404(List, pk=pk)
    lst.delete()
    url = reverse("reminders:index")
    return redirect(f"{url}?edit")
