from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework import mixins
from django.http import Http404
from rest_framework.views import APIView


from snippets.models import Snippet
from snippets.serializers import SnippetSerializer     
from rest_framework import generics, permissions
from snippets.permissions import IsOwnerOrReadOnly
from django.contrib.auth.models import User
from snippets.serializers import SnippetSerializer, UserSerializer
from rest_framework.permissions import AllowAny

"""
FBV → 
"""
# @api_view(['GET', 'POST'])
# def snippet_list(request,format=None):
#     if request.method == 'GET':
#         snippets = Snippet.objects.all()
#         serializer = SnippetSerializer(snippets, many=True)
#         return Response(serializer.data)
    
#     elif request.method == 'POST':
#         serializer = SnippetSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



# @api_view(['GET', 'PUT', 'DELETE'])
# def snippet_detail(request, pk , format=None):
#     try:
#         snippet = Snippet.objects.get(pk=pk)
#     except Snippet.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)

#     if request.method == 'GET':
#         serializer = SnippetSerializer(snippet)
#         return Response(serializer.data)

#     elif request.method == 'PUT':
#         serializer = SnippetSerializer(snippet, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     elif request.method == 'DELETE':
#         snippet.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


"""
CBV 전환
"""
# class SnippetList(APIView):
#     def get(self, request, format=None):
#         snippets = Snippet.objects.all()
#         serializer = SnippetSerializer(snippets, many=True)
#         return Response(serializer.data)
    
#     def post(self, request, format=None):
#         serializer = SnippetSerializer(data=request.data)
    
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#상세보기
# class SnippetDetail(APIView):
#     def get_object(self, pk):
#         try:
#             return Snippet.objects.get(pk=pk)
#         except Snippet.DoesNotExist:
#             raise Http404
        
#     def get(self, request, pk, format=None):
#         snippet = self.get_object(pk)
#         serializer = SnippetSerializer(snippet)
#         return Response(serializer.data)
    
#     def put(self, request, pk, format=None):
#         snippet = self.get_object(pk)
#         serializer = SnippetSerializer(snippet, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
#     def delete(self, request, pk, format=None):
#         snippet = self.get_object(pk)
#         snippet.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
        


"""
Mixin을 활용한 코드 재사용
"""                             
# class SnippetList(mixins.ListModelMixin,
#                   mixins.CreateModelMixin,
#                   generics.GenericAPIView
# ):
#     queryset = Snippet.objects.all()
#     serializer_class = SnippetSerializer

#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)

#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)
                
                
# class SnippetDetail(mixins.RetrieveModelMixin,
#                     mixins.UpdateModelMixin,
#                     mixins.DestroyModelMixin,
#                     generics.GenericAPIView):
#      queryset = Snippet.objects.all()
#      serializer_class = SnippetSerializer
     
#      def get(self, request, *args, **kwargs):
#          return self.retrieve(request, *args, **kwargs)           
    
#      def put(self, request, *args, **kwargs):
#          return self.update(request, *args, **kwargs)            
     
#      def delete(self, request, *args, **kwargs):
#         #return self.destroy(request, *args, **kwargs)
#         instance = self.get_object()  # 삭제할 객체 가져오기
#         self.perform_destroy(instance)  # 실제 삭제
#         return Response({"message": "delete success"}, status=status.HTTP_204_NO_CONTENT)


"""
완성형 GenericView로 최적화
"""    


# ✨ Snippet 목록 조회(GET), 생성(POST) View
class SnippetList(generics.ListCreateAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    
    # 인증된 사용자만 쓰기 가능, 비인증 사용자는 읽기만 가능
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    
    # POST 요청 시, 현재 요청한 사용자를 Snippet의 소유자로 저장
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
    

# ✨ Snippet 단건 조회(GET), 수정(PUT), 삭제(DELETE) View
class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
     
     # 인증된 사용자만 쓰기 가능 + 오직 소유자만 수정/삭제 가능
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    
    
    
# ✨ 모든 사용자 목록 조회 View
class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
# ✨ 특정 사용자 정보 조회 View (pk로 지정)
class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer    
    
    
    
    
# 회원가입 (User 생성)
class UserCreate(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]    