from rest_framework import serializers
from urlshortner.models import Url


class UrlSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Url
        fields = ('url', 'slug',)


class UrlDetailSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Url
        fields = ('id', 'url', 'slug', 'created')
