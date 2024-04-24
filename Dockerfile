FROM python

RUN mkdir -p /home/app
RUN pip install --no-cache-dir nltk
RUN pip install --no-cache-dir pandas

WORKDIR /home/app 

COPY . /home/app 



# /home/app/text_proccessing.py dah keda msar el file ely esmo text_proccessing 3shan ana 5las na2lto aw 7ateto gwa el folder ely esmo app ely mawgood gwa el container 3shan ana 2olt COPY . /home/app 
CMD ["python3","/home/app/text_proccessing.py"]



