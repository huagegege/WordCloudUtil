#!/bin/bash

cd `dirname $0`
python3 ../src/WordCloudUtil.py
open ./render.html