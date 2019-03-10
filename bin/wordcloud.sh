#!/bin/bash

while [[ -n "$1" ]]
do
  case "$1" in
    -url)
        web_url=$2
        shift
        ;;
    -file)
        file_path=$2
        shift
        ;;
    *)
        echo "$1 不是一个有效的参数"
        ;;
  esac
  shift
done

cd `dirname $0`
python3 ../src/WordCloudUtil.py --url=$web_url
open ./render.html