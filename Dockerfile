FROM nonpci-peg-dockreg01.prod.cdps.local:5000/alpine-python:2
MAINTAINER henka@protonmail.com
ARG proxy
ENV https_proxy=$proxy \
	LANG=en_US.UTF-8 \
	LC_ALL=en_US.UTF-8
COPY src /apps
WORKDIR /apps
RUN python -V
RUN pip install cryptography && pip install pipenv && pipenv install
CMD ["sh","/apps/bootstrap.sh"]
