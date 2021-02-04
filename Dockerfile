FROM python:3.7.4
WORKDIR /app
COPY ./ ./
RUN pip install -r requirements.txt
EXPOSE 8000
CMD ["uvicorn", "main:app","--reload", "--host","0.0.0.0"]