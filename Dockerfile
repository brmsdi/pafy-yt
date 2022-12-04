FROM python:3.7.15-alpine3.17 as compiler
ENV PYTHONUNBUFFERED 1

WORKDIR /app/

RUN python -m venv /opt/venv
# Enable venv
ENV PATH="/opt/venv/bin:$PATH"

RUN apk update && \
  apk add git && \
  pip3 install youtube-dl && \
  pip3 install git+https://github.com/brmsdi/pafy

COPY ./requirements.txt /app/requirements.txt
RUN pip3 install -Ur requirements.txt

FROM python:3.7.15-alpine3.17 as runner
WORKDIR /app/
COPY --from=compiler /opt/venv /opt/venv

# Enable venv
ENV PATH="/opt/venv/bin:$PATH"
COPY . /app/
RUN chmod 777 server.sh
ENTRYPOINT ["./server.sh"]