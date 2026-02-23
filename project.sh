#!/bin/bash

# bash utils

if [[ "$1" == "dev" ]]; then
    fastapi dev app/main.py
fi

if [[ "$1" == "prod" ]]; then
    fastapi run app/main.py
fi

if [[ "$1" == "package" ]] then
    pip-compile requirements.in > requirements.txt
fi