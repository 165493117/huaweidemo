FROM python:3.6 
WORKDIR /home/app/
COPY . .
CMD [ "python", "./app.py" ]