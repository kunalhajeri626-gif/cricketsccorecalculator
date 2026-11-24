FROM python:3.12
WORKDIR /app
COPY . .
CMD ["python3", "cricket_score.py", "160", "17.5", "72", "44", "195", "2.5"]
