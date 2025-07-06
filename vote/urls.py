from django.urls import path
from . import views

urlpatterns = [
    path('', views.project_list, name='project_list'),
    path('project/<int:project_id>/', views.project_detail, name='project_detail'),
    path('vote/', views.vote_all, name='vote_all'),
    path('results/', views.results, name='results'),
]
