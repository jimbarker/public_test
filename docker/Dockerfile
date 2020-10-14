FROM python:3.10.0a1-alpine3.12

RUN apt-get -y update && apt-get -y upgrade
# RUN apk add --no-cache jq
RUN apt install -y jq
RUN apt install -y git

# COPY assume-role /
COPY requirements.txt /tmp

RUN pip install --trusted-host=pypi.python.org --trusted-host=pypi.org --trusted-host=files.pythonhosted.org --no-cache-dir -r /tmp/requirements.txt

# CMD ["sh", "-c", "source /assume-role && aws --version"]
