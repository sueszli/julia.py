
ARG BASE_CONTAINER=jupyter/scipy-notebook
FROM $BASE_CONTAINER

LABEL maintainer="SaHu <hunold@par.tuwien.ac.at>"

USER root

RUN DEBIAN_FRONTEND=noninteractive apt-get update && \
     apt-get install -y imagemagick --no-install-recommends && \
     rm -rf /var/lib/apt/lists/*

USER $NB_UID

RUN python3 -m pip install parsl && \
  fix-permissions /home/$NB_USER
  
