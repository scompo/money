#!/bin/bash

# tests.sh

docker run -it --rm -v $(pwd):/money -w /money python:3 python3 -m unittest -v