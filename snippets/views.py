from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt # CSRF 검사를 비활성화하기 위한 데코레이터 임포트
from rest_framework.parsers import JSONParser # JSON 데이터를 파싱하기 위한 DRF(JSONParser) 임포트
from snippets.models import Snippet # Snippet 모델과 그에 대한 시리얼라이저 임포트
from snippets.serializers import SnippetSerializer


# CSRF 검사를 생략한 뷰 함수 정의
@csrf_exempt
def snippet_list(request):
    # HTTP 메서드가 GET일 경우, 모든 Snippet 객체를 조회하여 JSON으로 반환
    if request.method == 'GET':
        snippets = Snippet.objects.all()  # 모든 Snippet 객체 조회
        serializer = SnippetSerializer(snippets, many=True)  # 여러 객체 직렬화
        return JsonResponse(serializer.data, safe=False)  # 직렬화된 데이터를 JSON으로 응답

    # HTTP 메서드가 POST일 경우, 새 Snippet 객체를 생성
    elif request.method == 'POST':
        data = JSONParser().parse(request)  # 요청의 JSON 데이터를 파싱
        serializer = SnippetSerializer(data=data)  # 파싱된 데이터를 시리얼라이저에 전달
        if serializer.is_valid():  # 데이터 유효성 검사
            serializer.save()  # 유효하면 저장
            return JsonResponse(serializer.data, status=201)  # 생성된 객체를 JSON으로 응답
        return JsonResponse(serializer.errors, status=400)  # 유효하지 않으면 에러 반환

# 특정 Snippet 객체에 대한 조회, 수정, 삭제 처리 함수
@csrf_exempt
def snippet_detail(request, pk):
    try:
        snippet = Snippet.objects.get(pk=pk)  # 주어진 pk로 Snippet 객체 조회
    except Snippet.DoesNotExist:  # 객체가 존재하지 않을 경우
        return HttpResponse(status=404)  # 404 Not Found 응답

    # GET 요청일 경우, 해당 Snippet 객체를 JSON으로 반환
    if request.method == 'GET':
        serializer = SnippetSerializer(snippet)
        return JsonResponse(serializer.data)

    # PUT 요청일 경우, 기존 객체를 수정
    elif request.method == 'PUT':
        data = JSONParser().parse(request)  # 요청 데이터 파싱
        serializer = SnippetSerializer(snippet, data=data)  # 기존 객체와 새 데이터로 시리얼라이저 생성
        if serializer.is_valid():  # 유효성 검사
            serializer.save()  # 수정 내용 저장
            return JsonResponse(serializer.data)  # 수정된 객체 반환
        return JsonResponse(serializer.errors, status=400)  # 유효하지 않으면 에러 반환

    # DELETE 요청일 경우, 해당 객체 삭제
    elif request.method == 'DELETE':
        snippet.delete()  # 객체 삭제
        return HttpResponse(status=204)  # 204 No Content 응답
