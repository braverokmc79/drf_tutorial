from django.urls import path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns


app_name = "snippets"  # 네임스페이스 지정
  
  
urlpatterns = [

    path('', views.SnippetList.as_view(), name='snippet-list'),
    path('<int:pk>/', views.SnippetDetail.as_view()),

]


urlpatterns = format_suffix_patterns(urlpatterns)