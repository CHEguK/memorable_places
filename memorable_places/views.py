''' memorable_places/views '''
from django.shortcuts import render


def home(request):
    ''' View of home page '''
    return render(request, 'home.html')
