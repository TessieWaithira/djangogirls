from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Gist


# Create your views here.
def publish_read(request):
    gists = Gist.objects.all()
    return render(request, 'myreads/publish_read.html', context={'gists': gists})


def gist_detail(request, pk):
    gist = get_object_or_404(Gist, pk=pk)
    return render(request, 'myreads/gist_detail.html', {'gist': gist})
