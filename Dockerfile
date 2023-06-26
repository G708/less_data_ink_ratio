FROM ubuntu:latest

ENV PYTHON_VERSION 3.10.6
ENV HOME /root
ENV PYTHON_ROOT $HOME/local/python-$PYTHON_VERSION
ENV PATH $PYTHON_ROOT/bin:$PATH
ENV PYENV_ROOT $HOME/.pyenv

# タイムゾーン
RUN ln -sf /usr/share/zoneinfo/Asia/Tokyo /etc/localtime

# apt
RUN apt-get update
RUN apt-get install -y libopencv-dev

# install python and pip
RUN apt-get install -y python3 python3-pip
RUN pip install --upgrade pip

# set working directory and copy files
WORKDIR /usr/src/app
COPY ./ /usr/src/app

# install opencv
RUN pip install opencv-python

COPY requirement.txt ./

RUN pip install --upgrade setuptools
RUN pip install --no-cache-dir -r requirement.txt
