#!/bin/bash
activate () {
    . ./venv/bin/activate
}
activate

# set environmental variables
source .db_credentials

# create flask app name
export FLASK_APP=track_workout

# install package
pip install -e .
