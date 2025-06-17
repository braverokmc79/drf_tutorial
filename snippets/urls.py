from django.urls import path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns


app_name = "snippets"  # 네임스페이스 지정
  
  
urlpatterns = [
    path("snippets/", views.snippet_list),
    path("snippets/<int:pk>/", views.snippet_detail),
]


urlpatterns = format_suffix_patterns(urlpatterns)