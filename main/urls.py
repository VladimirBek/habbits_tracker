from django.urls import path
from .apps import MainConfig
from . import views


app_name = MainConfig.name


urlpatterns = [
    path('', views.HabitsListView.as_view(), name='habits_list'),
    path('public-habits/', views.PublicHabitsListView.as_view(), name='public_habits_list'),
    path('create/', views.HabitsCreateView.as_view(), name='habits_create'),
    path('update/<int:pk>/', views.HabitsUpdateView.as_view(), name='habits_update'),
    path('delete/<int:pk>/', views.HabitsDeleteView.as_view(), name='habits_delete'),

]