FROM alpine:3.12

RUN apk update
RUN apk upgrade
RUN apk add jq
RUN apk add git
RUN apk add python3
RUN apk add py3-pip

# COPY assume-role /
COPY requirements.txt /tmp

# RUN pip install --trusted-host=pypi.python.org --trusted-host=pypi.org --trusted-host=files.pythonhosted.org --no-cache-dir -r /tmp/requirements.txt
RUN pip install --no-cache-dir -r /tmp/requirements.txt


# CMD ["sh", "-c", "source /assume-role && aws --version"]
