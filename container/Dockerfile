#Dockerfile for Jace
#Created by Joel Schooler
# Copyright Palo Alto Research Center 2017,2018


FROM jfloff/alpine-python:latest
RUN git clone https://docjoel:alpha1beta2\)@github.com/PARC/jace.git
WORKDIR /jace
#Contains all setup for python and dependencies.
RUN sh setup.sh
EXPOSE 8000
