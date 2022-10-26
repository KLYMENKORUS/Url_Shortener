import random
import string
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from .models import Url
from django.contrib import messages
from django.views.generic import DeleteView, ListView
from django.contrib.messages.views import SuccessMessageMixin


def index(request):
    return render(request, 'Url_Shortener/index.html')


def create_short_url(request):
    if request.method == 'POST':
        slug = ''.join(random.choice(string.ascii_letters)
                       for x in range(6))
        url = request.POST['url']
        new_url = Url(url=url, slug=slug)
        new_url.save()
        messages.success(request, 'New URL is created you can check in on view urls')
        return redirect('/')


class UrlList(ListView):
    template_name = 'Url_Shortener/url.html'
    queryset = Url.objects.all()
    context_object_name = 'url'


def detail_url(request, pk):
    url = get_object_or_404(Url, pk=pk)
    return render(request, 'Url_Shortener/detail_url.html', {'url': url})


class UrlDeleteView(SuccessMessageMixin, DeleteView):
    model = Url
    template_name = 'Url_Shortener/url_delete.html'
    success_message = 'URl successfully deleted!'
    success_url = reverse_lazy('urlshortner:index')

