from django.urls import path ,include
from rest_framework.urlpatterns import format_suffix_patterns
from . import views
from rest_framework.routers import DefaultRouter


# urlpatterns = [
#     path('snippets/', views.SnippetList.as_view(), name='snippet-list'),
#     path('snippets/<int:pk>/', views.SnippetDetail.as_view(), name='snippet-detail'),
#     path('users/', views.UserList.as_view(), name='user-list'),
#     path('users/<int:pk>/', views.UserDetail.as_view(), name='user-detail'),
#     path('', views.api_root, name='api-root'),
#     path('snippets/<int:pk>/highlight/', views.SnippetHighlight.as_view(), name='snippet-highlight'),
# ]

# urlpatterns = format_suffix_patterns(urlpatterns)


router = DefaultRouter()
router.register('snippets', views.SnippetViewSet, basename='snippet')
router.register('users', views.UserViewSet, basename='user')
urlpatterns = [
    path('', include(router.urls)),
]