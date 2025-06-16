# Django Todo 시스템 - DRF 기반

Django REST framework(DRF)를 활용한 간단한 Todo API 예제입니다.
이 프로젝트는 API 설계, 직렬화, 뷰셋, 라우팅 등 Django DRF의 기본을 학습하는 데 초점을 맞춥니다.

---

## 학습 추천 : [코담](https://codam.kr/)

### 파이썬·장고 웹개발 | 코담 - 코드에 세상을 담다

[![코담 소개 이미지](https://codam.kr/assets/images/og-image.jpg)](https://codam.kr/)

---

📘 **코담 DRF  문서 보기**
[https://codam.kr/DRF/DRF\_공식문서/01\_공식문서를%20통한%20설치/1.%20공식문서를%20통한%20DRF%20설치.html](https://codam.kr/DRF/DRF_%EA%B3%B5%EC%8B%9D%EB%AC%B8%EC%84%9C/01_%EA%B3%B5%EC%8B%9D%EB%AC%B8%EC%84%9C%EB%A5%BC%20%ED%86%B5%ED%95%9C%20%EC%84%A4%EC%B9%98/1.%20%EA%B3%B5%EC%8B%9D%EB%AC%B8%EC%84%9C%EB%A5%BC%20%ED%86%B5%ED%95%9C%20DRF%20%EC%84%A4%EC%B9%98.html)

---

## 화면 구성

### 📁 drf\_tutorial 플랫폼 규조 (VS Code 기준)

```
drf_tutorial/
├── snippets/                     # API 앱 디렉토리
├── tutorial/                     # Django 설정 디렉토리
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── db.sqlite3                    # SQLite 기본 DB
├── manage.py                     # Django 관리 명령어
├── requirements.txt              # 의존성 목록
└── README.md
```

---

## ⚙️ 개발 환경

* Python 3.12.3
* Django 5.2.1
* Django REST Framework
* 가상환경: `venv` 사용

---

## ▶️ 실행 방법

1. 가상환경 활성화:

```bash
# macOS/Linux
source venv/bin/activate

# Windows
venv\Scripts\activate
```

2. 패키지 설치:

```bash
pip install -r requirements.txt
```

3. 서버 실행:

```bash
python manage.py runserver
```

---

## 📆 DB 마이그리언션

```bash
# 1. 목록 변경 사항 탐지
python manage.py makemigrations

# 2. 실제 DB에 반영
python manage.py migrate

# 3. 반영 확인
python manage.py showmigrations
```

---

## 📦 Commit 메시지 컨벤션 (Conventional Commits)

복잡한 개발 과정을 관리하기 위해 [Conventional Commits](https://www.conventionalcommits.org/) 형식을 적용합니다.

### ✍️ 컨벤션 타입 예시

| 타입         | 설명                   |
| ---------- | -------------------- |
| `feat`     | 새로운 기능 추가            |
| `fix`      | 버그 수정                |
| `docs`     | 문서 변경 (README 등)     |
| `style`    | 코드 포맷팅, 세미콬론 누르기 등   |
| `refactor` | 코드 리파터링 (기능 변화 없음)   |
| `test`     | 테스트 코드 추가 또는 수정      |
| `chore`    | 빌드, 패키지 설정 등 기타 변경사항 |

### 💡 예시

```bash
git commit -m "feat: Todo 목록 조회 API 구현"
git commit -m "fix: 날짜 형식 오류 수정"
git commit -m "docs: README 업데이트"
git commit -m "style: 불필요한 공백 제거"
git commit -m "refactor: view 함수 분리"
git commit -m "test: Todo 생성 테스트 추가"
git commit -m "chore: requirements.txt 정리"
```

---

## 👨‍💼 Author

* **코담(Codam)**: [https://codam.kr](https://codam.kr)
* Django REST Framework 학습에 최적화된 자료 제공
