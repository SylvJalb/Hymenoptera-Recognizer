# Server-side implementation with Python
Starting from "Hymenoptera Recognizer" project, this fork add a possible server-side implementation to allow users to ask prediction for an image

## Pre-Trained Model
In this example we use original [pre-trained model](/Hymenoptera-Recognizer/models/yolov5m_v2.pt).

* ### [yolov5m_v2 (from original documentation)](../README.md#yolov5m_v2)

## Configuration to run `endPoint.py` on Ubuntu server:

### First of all read and install [yolov5 project](https://github.com/ultralytics/yolov5): follow [pypi.org_yolov5](https://pypi.org/project/yolov5/)
```bash
pip install yolov5
```

### Install [FLASK](https://flask.palletsprojects.com/en/2.2.x/)
```bash
pip install Flask
pip install -U flask-cors
```

### Install SCREEN
```bash
pip install screen
```

## Now you can run the below code from the folder where you saved `endPoint.py` and Machine Learning Model:
```bash
screen
flask --app endPoint run --host=0.0.0.0 --port 5001
```
---
---
# Client-side implementation
In "client-side" folder you can find a possible usage of this web service. After a rapid check on service status, user can:

* Select an image
* Send image selected to server for Model Analysis
* Read Model analysis results
* Check on response image model result boxes