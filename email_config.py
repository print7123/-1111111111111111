# -*- coding: utf-8 -*-
"""
이메일 설정 파일
네이버 메일 SMTP 설정을 관리합니다.

⚠️ 보안 주의사항:
- 이 파일은 .gitignore에 추가되어 있어야 합니다.
- 실제 비밀번호를 입력한 후 절대 공유하지 마세요.
"""

# 네이버 메일 SMTP 설정
MAIL_SERVER = 'smtp.naver.com'
MAIL_PORT = 587
MAIL_USE_TLS = True
MAIL_USERNAME = 'print7123@naver.com'

# ⚠️ 중요: 네이버 앱 비밀번호를 여기에 입력하세요
# 네이버 메일 → 환경설정 → 보안 → 2단계 인증 → 앱 비밀번호 생성
# 생성된 16자리 비밀번호를 아래에 입력하세요
MAIL_PASSWORD = '7B2C4JFE4J3L'  # 여기에 실제 앱 비밀번호 입력

# 설정 확인 함수
def is_password_set():
    """비밀번호가 실제로 설정되었는지 확인"""
    return MAIL_PASSWORD and MAIL_PASSWORD != 'your-app-password'


