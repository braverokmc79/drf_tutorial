from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    객체의 소유자만 수정/삭제 가능하게 하는 커스텀 권한 클래스
    """
    
    def has_object_permission(self, request, view, obj):
	    # 읽기 요청이면 (GET, HEAD, OPTIONS)
        if request.method in permissions.SAFE_METHODS:
            return True
        # 수정/삭제 요청이면: 객체의 소유자만 가능
        return obj.owner == request.user
