#!/usr/bin/env bash

workdir=$(cd `dirname $0`; pwd)
PATH="$PATH:$workdir"


while [[ -n "$1" ]]
do
  case "$1" in
    -keyword)
        keyword=$2
        shift
        ;;
    -pagesize)
        pagesize=$2
        shift
        ;;
    *)
        echo "$1 不是一个有效的参数"
        ;;
  esac
  shift
done

if [ ! -n "$pagesize" ]; then pagesize=20

fi

cd `dirname $0`
python3 ../src/WYWordCloudUtil.py --keyword=$keyword --pagesize=$pagesize
open ./render.html