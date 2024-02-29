FROM python:3.9 

WORKDIR /app

RUN pwd

COPY ../requirements.txt requirements.txt
RUN pip install -r requirements.txt 

COPY ../ src/ src/

EXPOSE 7860 

CMD ["python", "src/app.py"]  
