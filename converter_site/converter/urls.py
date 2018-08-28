from django.urls import path
from . import views

app_name = 'converter'
urlpatterns = [
    path('', views.index, name='index'),
    path('creature/', views.CreatureView.as_view(), name='creature'),
    # path('', views.IndexView.as_view(), name='index'),
    # path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    # path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    # path('<int:question_id>/vote/', views.vote, name='vote'),
]