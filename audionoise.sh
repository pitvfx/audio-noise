#!/bin/bash

# run audio-noise in python and parse all arguments
# usage: ./audionoise.sh [args]
# run python in virtual environment

cd "$(dirname "$0")"
source .venv/bin/activate
python audionoise "$@"