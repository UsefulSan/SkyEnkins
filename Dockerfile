FROM python

EXPOSE 8000

WORKDIR /django

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY . .

RUN bash -c "pip install -r requirements.txt"
