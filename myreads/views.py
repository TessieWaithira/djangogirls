from django.contrib.auth.decorators import login_required
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


@login_required
def gist_new(request):
    form = GistForm
    if request.method == 'POST':
        form = GistForm(request.POST)
        if form.is_valid():
            gist = form.save(commit=False)
            gist.user = request.user
            gist.save()
            return redirect('gist_detail', pk=gist.pk)
    else:
        form = GistForm()
    return render(request, 'myreads/gist_new.html', context={'form': form})


@login_required
def gist_edit(request, pk):
    gist = get_object_or_404(Gist, pk=pk)
    if request.method == "POST":
        form = GistForm(request.POST, instance=gist)
        if form.is_valid():
            gist = form.save(commit=False)
            gist.user = request.user
            gist.save()
            return redirect('gist_detail', pk=gist.pk)
    else:
        form = GistForm(instance=gist)
    return render(request, 'myreads/gist_edit.html', context={'form': form})


@login_required
def gist_draft_list(request):
    gists = Gist.objects.filter(published_date__isnull=True).order_by('created_date')
    return render(request, 'myreads/gist_draft_list.html', {'gists': gists})


@login_required
def gist_publish(request, pk):
    gist = get_object_or_404(Gist, pk=pk)
    gist.publish()
    return redirect('gist_detail', pk=gist.pk)


@login_required
def gist_delete(request, pk):
    gist = get_object_or_404(Gist, pk=pk)
    gist.delete()
    return redirect('publish_read')
