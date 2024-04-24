FROM python

RUN mkdir -p /home/app
RUN pip install --no-cache-dir nltk
RUN pip install --no-cache-dir pandas

WORKDIR /home/app 

COPY . /home/app 

CMD ["python3","/home/app/text_proccessing.py"]



