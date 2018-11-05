from django.urls import path

from . import views

app_name = 'testapp'    #アプリの名前空間定義。templateからURLを正確に判断するためのもの
urlpatterns = [
    #path('', views.index, name='index'),

    #path('<int:question_id>/', views.detail, name='detail'),
    #path('<int:question_id>/results/', views.results, name='results'),
#------------------------------------------------------------------------------------------------
# 以下は汎用ビューを使った書き方
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),

    path('<int:question_id>/vote/', views.vote, name='vote'),
]
