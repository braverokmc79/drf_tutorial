from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect
from snippets.views import UserCreate, UserList, UserDetail
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path("admin/", admin.site.urls),
    
    
    path("", lambda request: redirect("snippets:snippet-list")),
     
    # Django 로그인/로그아웃용 (DRF UI 로그인)
    path("api-auth/", include("rest_framework.urls")),

    # API: /snippets/, /snippets/<id>/
    path("snippets/", include("snippets.urls")),

    # API: /users/, /users/<id>/
    path('users/', UserList.as_view()),
    path('users/<int:pk>/', UserDetail.as_view()),
    #회원가입
    path('register/', UserCreate.as_view(), name='user-register'),
    
    # 로그인 후 리디렉션
    path("accounts/profile/", lambda request: redirect("snippets:snippet-list")),
    
    
    #path('api-token-auth/', obtain_auth_token),
]
