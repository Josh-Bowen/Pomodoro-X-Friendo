#!/bin/bash
if ! [[ -x "$(command -v python)" ]]
then
    echo "Error:
        no good... Install python at https://www.python.org/" >&2
    exit 1
else
    python3 main.py
fi