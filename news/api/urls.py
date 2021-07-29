from django.conf.urls import url
from django.urls import path
from news.api import views as api_views

urlpatterns = [
    path('Articles/',api_views.Article_list_API_VIEW.as_view(),name='articles'),
    path('Journalists/',api_views.Journalists_list_API_VIEW.as_view(),name='journalists'),
    path('Articles/<int:pk>/',api_views.Article_Detail_API_VIEW.as_view(),name='detail_article'),
]
