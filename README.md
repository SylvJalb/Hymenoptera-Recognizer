# Hymenoptera Recognizer
## Train the Yolo model
```bash
cd dataset
unzip Hymenoptera.v2i.yolov5pytorch.zip
git clone git@github.com:ultralytics/yolov5.git
cd yolov5
python train.py --img 640 --batch 16 --epochs 100 --data ../dataset/Hymenoptera.v2i.yolov5pytorch/data.yaml --weights yolov5m.pt
```
(You can add `--device cpu` to use CPU. Default is GPU.)

# Validate the Yolo model
You can see the train and validate results in `yolov5/runs/train/exp`.    
If the model looks good, you can run the following command before use it:
```bash
mv ./yolov5/runs/train/exp/weights/best.pt ./models/yolov5m.pt
```

# Use the Yolo model
