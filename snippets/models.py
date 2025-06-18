from django.db import models
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles # Pygments에서 사용 가능한 모든 스타일(코드 하이라이팅 스타일)을 가져오는 함수
from django.contrib.auth.models import User
from pygments.lexers import get_lexer_by_name
from pygments.formatters.html import HtmlFormatter
from pygments import highlight


"""
Pygments는 파이썬 기반의 문법 하이라이터(Syntax Highlighter) 라이브러리입니다. 
주로 프로그래밍 코드나 마크다운 문서에서 코드를 색상별로 보기 좋게 표시할 때 사용됩니다.
"""

LEXERS = [item for item in get_all_lexers() if item[1]] # 사용 가능한 lexer 중에서 identifier가 존재하는 항목만 필터링하여 리스트로 저장
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS]) # LANGUAGE_CHOICES는 (코드, 언어 이름) 형식의 튜플로 구성된 리스트. 예: ('python', 'Python')
# STYLE_CHOICES는 Pygments 스타일 이름을 (이름, 이름) 형식의 튜플로 리스트화. 예: ('friendly', 'friendly')
STYLE_CHOICES = sorted([(item, item) for item in get_all_styles()])


# 코드 스니펫(Snippet)을 나타내는 Django 모델 클래스 정의
class Snippet(models.Model):
    created = models.DateTimeField(auto_now_add=True)     # 생성 시각 자동 저장   
    title = models.CharField(max_length=100, blank=True, default='') # 코드 스니펫 제목 (옵션, 기본값 '')
    code = models.TextField()    # 코드 내용 저장 필드
    linenos = models.BooleanField(default=False)     # 줄 번호 표시 여부
    language = models.CharField(choices=LANGUAGE_CHOICES, default='python', max_length=100)    # 	코드의 프로그래밍 언어 (선택지 있음), LANGUAGE_CHOICES에서 선택 (기본: python)
    style = models.CharField(choices=STYLE_CHOICES, default='friendly', max_length=100)     # 코드 스타일 선택 필드, STYLE_CHOICES에서 선택 (기본: friendly)
     
       # 새로 추가된 필드
    owner = models.ForeignKey(User, related_name='snippets', on_delete=models.CASCADE)
    highlighted = models.TextField()
   
    class Meta:      
        ordering = ['created'] # 이 모델 인스턴스의 기본 정렬 기준을 created 필드로 설정

    # 코드 저장 시 자동으로 하이라이트 처리
    def save(self, *args, **kwargs):
        lexer = get_lexer_by_name(self.language)
        linenos = 'table' if self.linenos else False
        options = {'title': self.title} if self.title else {}
        formatter = HtmlFormatter(style=self.style, linenos=linenos, full=True, **options)
        self.highlighted = highlight(self.code, lexer, formatter)
        super().save(*args, **kwargs)