#Dockerfile for Jace
#Created by Joel Schooler


FROM alpine-python:latest
RUN git clone https://docjoel:alpha1beta2\)@github.com/PARC/jace.git
WORKDIR /jace
#Contains all setup for python and dependencies.
RUN sh setup.sh
EXPOSE 8000
WORKDIR /jace
ENTRYPOINT ./run_local