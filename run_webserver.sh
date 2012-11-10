#!/bin/bash

export PYTHONPATH=${PYTHONPATH:+$PYTHONPATH:}$(pwd)

exec ./web_frontend/web.py "$@"
