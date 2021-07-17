#!/bin/bash
if ! [[ -x "$(command -v python)" ]]
then
    echo "Error:
        no good... Install python at https://installpython3.com" >&2
    exit 1
else
    python3 main.py
fi