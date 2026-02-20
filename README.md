# 온누리인쇄나라 웹사이트

온누리인쇄나라의 공식 웹사이트입니다. Flask 기반으로 제작되었습니다.

## 주요 기능

- 📋 견적 계산 시스템
- 📸 포트폴리오 관리
- 💬 Q&A 게시판
- 📧 이메일 문의
- 👤 관리자 대시보드

## 설치 방법

### 1. 필수 패키지 설치

```bash
pip install -r requirements.txt
```

### 2. 환경 설정

`email_config.py` 파일을 생성하고 이메일 설정을 추가하세요:

```python
MAIL_SERVER = 'smtp.naver.com'
MAIL_PORT = 587
MAIL_USE_TLS = True
MAIL_USERNAME = 'your-email@naver.com'
MAIL_PASSWORD = 'your-app-password'
```

### 3. 데이터베이스 초기화

애플리케이션을 처음 실행하면 자동으로 데이터베이스가 생성됩니다.

### 4. 서버 실행

```bash
python app_enhanced_작동중.py
```

또는

```bash
python 서버_시작.bat
```

## 접속 정보

- 기본 URL: http://localhost:5000
- 관리자 ID: admin
- 관리자 PW: admin123

## 프로젝트 구조

```
홈페이지_최종분_26.02.11/
├── app_enhanced_작동중.py    # 메인 Flask 애플리케이션
├── templates/                 # HTML 템플릿
├── static/                    # 정적 파일 (CSS, JS, 이미지)
│   ├── css/
│   ├── js/
│   └── images/
├── instance/                  # 데이터베이스 (자동 생성)
├── uploads/                   # 업로드 파일 (자동 생성)
└── requirements.txt           # 필수 패키지 목록
```

## 기술 스택

- **Backend**: Flask (Python)
- **Database**: SQLite
- **Frontend**: HTML, CSS, JavaScript, Bootstrap
- **Email**: SMTP (네이버 메일)

## 라이선스

이 프로젝트는 온누리인쇄나라의 소유입니다.

## 문의

- 전화: 02-6338-7123
- 이메일: print7123@naver.com
- 웹사이트: https://print7123.com/

---

© 2026 온누리인쇄나라. All rights reserved.
