from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
from django.utils import timezone
from .forms import GistForm
from .models import Gist


# Create your views here.
def publish_read(request):
    gists = Gist.objects.all()
    return render(request, 'myreads/publish_read.html', context={'gists': gists})


def gist_detail(request, pk):
    gist = get_object_or_404(Gist, pk=pk)
    return render(request, 'myreads/gist_detail.html', {'gist': gist})


def gist_new(request):
    form = GistForm
    if request.method == 'POST':
        form = GistForm(request.POST)
        if form.is_valid():
            gist = form.save(commit=False)
            gist.user = request.user
            gist.date = timezone.now()
            gist.save()
            return redirect('gist_detail', pk=gist.pk)
    else:
        form = GistForm()
    return render(request, 'myreads/post_new.html', context={'form': form})
