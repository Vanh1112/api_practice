# api_practice
create api using fastAPI

docker build -t api_practice:latest .

docker run -itd -v $PWD:/app -p 8000:8000 --name api_practice api_practice:latest