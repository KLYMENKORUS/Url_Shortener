from django.urls import path
from . import views


urlpatterns = [
    path('urls/', views.url_list),
    path('urls/<int:pk>/', views.url_detail)
]