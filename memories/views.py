''' memories/views.py '''
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse
from django.views import View
from django.views.generic import ListView
from django.views.generic.detail import DetailView

from memories.forms import MemoryItemForm
from memories.models import MemoryItem


@login_required
def index(request):  # pylint: disable=unused-argument
    ''' Index '''
    return HttpResponse('Ваши воспоминания Туть')


class MemoriesListView(ListView):
    ''' Memories List View '''
    queryset = MemoryItem.objects.all()  # pylint: disable=no-member
    context_object_name = 'memories'
    template_name = "memories/list.html"

    def get_queryset(self):
        ''' Get queryset '''
        user = self.request.user
        if user.is_anonymous:
            return []
        return user.memories.all()


class MemoriesCreateView(View):
    ''' Memories Create View '''
    @classmethod
    def my_render(cls, request, form, **kwargs):
        ''' Render method '''
        return render(request, "memories/create.html", {"form": form,
                                                        "mapbox_token": kwargs['mapbox_token']})

    def post(self, request):
        ''' Post '''
        form = MemoryItemForm(request.POST)
        if form.is_valid():
            new_memory = form.save(commit=False)
            new_memory.owner = request.user
            new_memory.save()
            return redirect(reverse(viewname="memories:list"))
        return self.my_render(request, form)

    def get(self, request):
        ''' Get '''
        form = MemoryItemForm()
        return self.my_render(request, form, mapbox_token=settings.MAPBOX_TOKEN)


class MemoryDetailsView(DetailView):
    ''' Memory Details View '''
    model = MemoryItem
    template_name = 'memories/details.html'


def delete_memory(request, uid):  # pylint: disable=unused-argument
    ''' Delete memory '''
    memory = MemoryItem.objects.get(id=uid)  # pylint: disable=no-member
    memory.delete()
    return redirect(reverse(viewname="memories:list"))
