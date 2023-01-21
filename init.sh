#!/bin/sh

CONFIG=${1}

mkdir -p assets/$CONFIG 
mkdir -p corpus/$CONFIG
mkdir -p training/$CONFIG

if [ CONFIG == "production"];
then
    pip install -U ja_ginza_electra
else
    pip install -U ja_ginza
fi

