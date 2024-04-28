from django.shortcuts import get_object_or_404, render

from .models import *

# Create your views here.


def details(request, pk):
    item = get_object_or_404(Item, pk=pk)
    # pdf = Item.object.all()

    return render(request, 'details.html',{
        'item': item,
    })