FROM alpine:3.12

RUN apk --update --no-cache add fuse alpine-sdk fuse-dev bash python3 py3-pip samba-client; \
    pip3 install --upgrade setuptools pip validators; \
    rm -rf /var/cache/apk/*;

COPY run.py /run.py
CMD python3 /run.py && tail -f /dev/null
