FROM busybox:1.36

RUN adduser -D picard
USER picard
WORKDIR /home/picard

COPY --chown=picard:picard . .

RUN echo "I:picard_talk.html" >> httpd.conf

CMD ["busybox", "httpd", "-f", "-v", "-p", "1701"]
