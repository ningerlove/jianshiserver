#!/bin/bash
gpu_id=$1
echo $gpu_id




docker run --rm --shm-size=64g -it -w /mnt/media3/liuning/code/python_code/jianshiserver -p 7942:7942 -p 7733:7733  -e MYSQL_ROOT_PASSWORD=123456 --name  jianshiserver -v /:/mnt jianshi_server_liuning_5_7_35:latest bash