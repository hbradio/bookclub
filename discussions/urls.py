from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:discussion_id>/', views.discussion_detail, name='discussion_detail'),
]