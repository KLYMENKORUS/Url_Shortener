from django.db import models
from django.urls import reverse_lazy


class Url(models.Model):
    url = models.URLField(max_length=200)
    slug = models.CharField(max_length=15)
    created = models.DateField(auto_now_add=True)

    def get_absolute_url(self):
        return reverse_lazy('urlshortner:url_detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.url

