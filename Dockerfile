FROM python:latest

WORKDIR /bot

RUN pip install virtualenv
RUN virtualenv -p python3 /bot
RUN /bin/bash -c "source /bot/bin/activate && pip install zulip-bots"

COPY $CI_PROJECT_DIR/src/ /bot/

CMD ["/bin/bash","-c","source /bot/bin/activate && zulip-run-bot randy.py"]