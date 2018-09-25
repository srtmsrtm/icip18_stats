FROM ubuntu:18.04
#FROM nvidia/cuda:9.2-cudnn7-devel-ubuntu18.04
MAINTAINER srtmsrtm
LABEL OBJECT="icip2018 stats"
ARG http_proxy
ARG https_proxy
ENV http_proxy ${http_proxy}
ENV https_proxy ${https_proxy}
ENV DEBIAN_FRONTEND noninteractive

# packages
RUN apt -y update
RUN apt -y upgrade
RUN apt install -y --no-install-recommends apt-utils
RUN apt install -y --no-install-recommends apt-transport-https ca-certificates
RUN apt install -y --no-install-recommends software-properties-common
RUN apt install -y language-pack-ja-base language-pack-ja
RUN apt install -y build-essential checkinstall
RUN apt install -y zlib1g-dev unzip libssl-dev curl git wget
RUN apt install -y libbz2-dev libreadline-dev libsqlite3-dev
RUN apt install -y cmake libgtk2.0-dev pkg-config libavcodec-dev libavformat-dev libswscale-dev
RUN apt install -y libtbb2 libtbb-dev libjpeg-dev libpng-dev libtiff-dev libdc1394-22-dev
RUN apt install -y libeigen3-dev libarpack2-dev
RUN apt install -y libblas-dev liblapack-dev
RUN apt install -y liblog4cxx-dev libhdf5-dev
#RUN apt install -y ffmpeg x264 x265
RUN apt install -y vim
COPY .vimrc /root/
RUN apt -y update
RUN apt -y upgrade

# locale
ENV LANG en_US.UTF-8  
ENV LANGUAGE en_US:en  
ENV LC_ALL en_US.UTF-8
RUN locale-gen en_US.UTF-8

# pyenv & python 3.6.3
RUN git clone https://github.com/yyuu/pyenv.git /root/.pyenv
ENV HOME /root
ENV PYENV_ROOT $HOME/.pyenv
ENV PATH $PYENV_ROOT/bin:$PATH
RUN echo 'export PYENV_ROOT="$HOME/.pyenv"' >> /root/.bashrc
RUN echo 'export PATH="$PYENV_ROOT/bin:$PYENV_ROOT/shims:$PATH"' >> /root/.bashrc
RUN echo 'eval "$(pyenv init -)"' >> /root/.bashrc
RUN ["/bin/bash", "-c", "source /root/.bashrc"]
RUN pyenv install 3.6.3
RUN pyenv global 3.6.3
RUN pyenv rehash
RUN /root/.pyenv/shims/pip install numpy scipy matplotlib pandas h5py networkx pytube opencv-python pillow wordcloud lxml

#
COPY src /root/src
#RUN mkdir -p /root/src
#RUN git clone https://github.com/amueller/word_cloud /root/src/word_cloud
#RUN git clone https://github.com/pjreddie/darknet /root/src/darknet
#RUN wget https://pjreddie.com/media/files/yolov3.weights -O /root/src/darknet/yolov3.weights
#COPY ytvideos /root/ytvideos
#COPY Makefile /root/src/darknet/Makefile
#COPY run.py /root/src/darknet/run.py

