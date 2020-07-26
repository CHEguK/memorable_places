from django.shortcuts import render, redirect
from django.urls import reverse
from memories.models import MemoryItem
from memories.forms import MemoryItemForm
from django.views import View
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.contrib.auth.decorators import login_required
from django.conf import settings

@login_required
def index(request):
    return HttpResponse('Ваши воспоминания Туть')

class MemoriesListView(ListView):
    queryset = MemoryItem.objects.all()
    context_object_name = 'memories'
    template_name = "memories/list.html"

    def get_queryset(self):
        u = self.request.user
        if u.is_anonymous:
            return []
        return u.memories.all()

class MemoriesCreateView(View):
    def my_render(self, request, form, **kwargs):
        return render(request, "memories/create.html", {"form": form,
                                                        "mapbox_token": kwargs['mapbox_token']})

    def post(self, request, *args, **kwargs):
        form = MemoryItemForm(request.POST)
        if form.is_valid():
            new_memory = form.save(commit=False)
            new_memory.owner = request.user
            new_memory.save()
            return redirect(reverse(viewname="memories:list"))
        return self.my_render(request, form)

    def get(self, request, *args, **kwargs):
        form = MemoryItemForm()
        return self.my_render(request, form, mapbox_token=settings.MAPBOX_TOKEN)

class MemoryDetailsView(DetailView):
    model = MemoryItem
    template_name = 'memories/details.html'

def delete_memory(request, uid):
    m = MemoryItem.objects.get(id=uid)
    m.delete()
    return redirect(reverse(viewname="memories:list"))
