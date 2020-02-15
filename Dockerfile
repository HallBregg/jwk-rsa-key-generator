FROM python:3.8

RUN mkdir /keys
WORKDIR /tmp
RUN pip install authlib
COPY ./generator.py ./generator.py



ENV KEY_NUMBER=2
ENV RSA_SIZE=2048

CMD ["python", "generator.py"]