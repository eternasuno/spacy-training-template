#!/bin/sh

CONFIG=${1}

mkdir -p assets/${vars.config} 
mkdir -p corpus/${vars.config}
mkdir -p training/${vars.config}

if [ CONFIG == "production"];
then
    python -m spacy download ja-ginza-electra
else
    python -m spacy download ja-ginza

