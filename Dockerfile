FROM python:latest

WORKDIR /bot

COPY $CI_PROJECT_DIR/src/ /bot/