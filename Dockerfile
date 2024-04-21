FROM redhat/ubi8:8.9
WORKDIR /aem
COPY config.yml config.yml
COPY passwordfile.properties passwordfile.properties
COPY scripts scripts
COPY sdk sdk
RUN yum -y install python3
RUN pip3 install -r scripts/requirements.txt
RUN python3 scripts/sdk_extract.py author
RUN python3 scripts/sdk_extract.py publish
RUN yum -y install java-11-openjdk
# ENTRYPOINT [ "tail", "-f", "/dev/null" ] # use only in tests