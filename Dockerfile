FROM registry.downbox.co.uk/zulipbots/zulipbotbase

WORKDIR /app

ARG ZULIP_EMAIL
ARG ZULIP_API_KEY
ARG ZULIP_SITE
ARG CI_COMMIT_SHORT_SHA

COPY src/*.py ./

ENV ZULIP_EMAIL="$ZULIP_EMAIL" ZULIP_API_KEY="$ZULIP_API_KEY" ZULIP_SITE="$ZULIP_SITE" CI_COMMIT_SHORT_SHA="$CI_COMMIT_SHORT_SHA"

CMD ["/bin/bash","-c","source /app/bin/activate && zulip-run-bot randy.py"]
