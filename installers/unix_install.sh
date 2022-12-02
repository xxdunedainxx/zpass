#!/bin/bash

apt-get update

PYTHON_INTERPRETER=($(which python3 || which python))

pipInstall=$(python3 -m pip)

if [[ $? != 0 ]];
then
  echo "Installing pip..."
  sudo apt-get install python3-pip
fi

${PYTHON_INTERPRETER} -m pip install flask
${PYTHON_INTERPRETER} -m pip install Flask-Cors
${PYTHON_INTERPRETER} -m pip install PyCryptodome