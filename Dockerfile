# 1. 베이스 이미지: Python
FROM python:3.12

# 2. 작업 디렉토리 만들기
WORKDIR /app

# 3. requirements.txt 복사해서 설치
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 4. 전체 프로젝트 복사
COPY . .

# 5. 8000 포트 개방
EXPOSE 8000

# 6. 마이그레이션하고 서버 실행
CMD ["sh", "-c", "python manage.py migrate && python manage.py runserver 0.0.0.0:8000"]
