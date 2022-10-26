from django.urls import path
from . import views

app_name = 'urlshortner'

urlpatterns = [
    path('', views.index, name='index'),
    path('createshorturl/', views.create_short_url, name='create_short_url'),
    path('url/created', views.UrlList.as_view(), name='url_created'),
    path('url/<pk>/deleted/', views.UrlDeleteView.as_view(), name='url_deleted'),
    path('detail/<int:pk>/', views.detail_url, name='url_detail')
]