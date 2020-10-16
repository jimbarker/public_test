FROM alpine:3.12

RUN apk update
RUN apk upgrade
RUN apk add jq
RUN apk add git
RUN apk add python3
RUN apk add py3-pip

COPY requirements.txt /tmp
COPY md_bucket_list.py /

RUN pip install --no-cache-dir -r /tmp/requirements.txt
