#Dockerfile for Jace
#Created by Joel Schooler
#Copyright PARC 2016-17

#Get alpine-python
FROM alpine:latest
#get jace


RUN apk update
RUN apk add python3
RUN apk add gcc
RUN apk add git
RUN git clone https://docjoel:alpha1beta2\)@github.com/PARC/jace.git
#change directory to jace
WORKDIR /jace
#Contains all setup for python and dependencies.
RUN sh setup.sh
#make port 8000 open
EXPOSE 8000

#run server
RUN ./run_local

ENTRYPOINT ["./run_local"]
