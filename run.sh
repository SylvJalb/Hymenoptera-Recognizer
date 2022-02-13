#!/bin/bash

python ./yolov5/detect.py --weights ../models/$1.pt --source $2

mv ./yolov5/runs/detect/exp/* ./src/results/

rm -r ./yolov5/runs/detect/exp/