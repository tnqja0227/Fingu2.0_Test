FROM python:3.9  

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt 

COPY src/ src/

ENV OPENAI_API_KEY "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"  

EXPOSE 7860 

CMD ["python", "src/chatbot.py"] 
