# *************************************************************************
# *
# *  © [2018] PARC Inc., A Xerox Company
# *  All Rights Reserved.
# *
# * NOTICE:  All information contained herein is, and remains
# * the property of Xerox Corporation.
# * The intellectual and technical concepts contained
# * herein are proprietary to PARC Inc. and Xerox Corp.,
# * and may be covered by U.S. and Foreign Patents,
# * patents in process, and may be protected by copyright law.
# * This file is subject to the terms and conditions defined in
# * file 'LICENSE.md', which is part of this source code package.
# *
# **************************************************************************

# Dockerfile for Jace
# Created by Joel Schooler
# Copyright PARC 2016-17

#Get alpine
FROM alpine:latest

RUN apk update
RUN apk add python3
RUN apk add gcc
RUN apk add git
#get jace
RUN git clone https://github.com/PARC/jace.git
#change directory to jace
WORKDIR /jace
#Contains all setup for python and dependencies.
RUN sh setup.sh
#make port 8000 open
EXPOSE 8000

#run server

ENTRYPOINT ["./run_local"]

