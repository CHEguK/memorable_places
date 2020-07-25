from django.shortcuts import render, redirect
from django.urls import reverse
from memories.models import MemoryItem
from memories.forms import MemoryItemForm
from django.views import View
from django.views.generic import ListView


class MemoriesListView(ListView):
    queryset = MemoryItem.objects.all()
    context_object_name = 'memories'
    template_name = "memories/list.html"


class MemoriesCreateView(View):
    def post(self, request, *args, **kwargs):
        form = MemoryItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/memories/list")
        return render(request, "memories/create.html", {"form": form})

    def get(self, request, *args, **kwargs):
        form = MemoryItemForm()
        return render(request, "memories/create.html", {"form": form})


def add_memory(request):
    if request.method == "POST":
        name = request.POST["description"]
        m = MemoryItem(name=name)
        m.save()
    return redirect('/memories/list')
    