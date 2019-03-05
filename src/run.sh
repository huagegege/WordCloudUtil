#!/bin/bash

cd `dirname $0`
python3 ./wordcloudutil.py
open ./render.html