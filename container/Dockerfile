#Dockerfile for Jace
#Created by Joel Schooler
#Copyright PARC 2016-17

#Get alpine-python
FROM jfloff/alpine-python:latest
#get jace
RUN git clone https://docjoel:alpha1beta2\)@github.com/PARC/jace.git
#change directory to jace
WORKDIR /jace
#Contains all setup for python and dependencies.
RUN sh setup.sh
#make port 8000 open
EXPOSE 8000

#run server
RUN ./run_local

#from Dockerfile of alpine-python
ENTRYPOINT ["/usr/bin/dumb-init","./run_local"]
CMD ["./run_local"]