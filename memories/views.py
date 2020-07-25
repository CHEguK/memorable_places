from django.shortcuts import render, redirect
from django.urls import reverse
from memories.models import MemoryItem


def memories_list(request):
    all_memories = MemoryItem.objects.all()

    return render(
                request,
                'memories/list.html',
                {'memories': all_memories}
                )

def memories_create(request):
    return render(request, 'memories/create.html',)
    