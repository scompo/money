#!/bin/bash

# shell.sh

docker run -it --rm -v $(pwd):/money -w /money  python:3 /bin/bash