#!/bin/bash
activate () {
    . ./venv/bin/activate
}
activate

# install package
pip install -e .

# create flask app name
export FLASK_APP=track_workout