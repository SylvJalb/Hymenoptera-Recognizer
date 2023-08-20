import yolov5

# First of all load pre-trained model 'Hymenoptera-Recognizer'
print('Model Loading...')
model = yolov5.load('./model/yolov5m_v2.pt')
print('Model Loaded!')
  
# Set model parameters
model.conf = 0.25  # NMS confidence threshold
model.iou = 0.45  # NMS IoU threshold
model.agnostic = False  # NMS class-agnostic
model.multi_label = False  # NMS multiple labels per box
model.max_det = 20  # maximum number of detections per image


from flask import Flask, request
from flask_cors import CORS
import shutil
import base64
import json

counter = -1

myEndPoint = Flask(__name__)
cors = CORS(myEndPoint)

@myEndPoint.route("/api/v2/test", methods = ['GET'])
def test():
    return {"status": "Service Up!"}, 200

@myEndPoint.route("/api/v2/img/inference", methods = ['POST'])
def predict_image():
    global counter

    # Check if the post request has the file part
    if 'userImage' not in request.files:
        return {"error": "NO FILE"}, 415

    # Get image
    img = request.files['userImage']
    img.save("inputImage")

    # Perform inference
    yoloPrediction = model("inputImage")

    # Parse results
    predictions = yoloPrediction.pred[0]
    # boxes = predictions[:, :4] # x1, y1, x2, y2
    scores = predictions[:, 4]
    categories = predictions[:, 5]

    #Dictionary for categories found
    outputDictionary = {}

    #Analysis of predictions
    for index, cat in enumerate(categories):
        type = ""
        
        if 0. in cat:
            type = "Ape"                                #red
        if 1. in cat:
            type = "Vespa"                              #pink
        if 2. in cat:
            type = "Calabrone Europeo"                  #orange
        if 3. in cat:
            type = "Vespa Orientale"                    #light orange
        if 4. in cat:
            type = "Velutina (Calabrone Asiatico)"      #yellow

        outputDictionary[str(index)] = type + "_" + str(scores[index])[7:14]   

    #yoloPrediction.show()

    image_file = 'responseImage.jpg'
    # Save results
    yoloPrediction.save(image_file)

    #Bytes convertion
    with open(image_file, "rb") as f:
        im_bytes = f.read()        
    im_b64 = base64.b64encode(im_bytes).decode("utf8")

    #Delete export folder
    shutil.rmtree("./runs")

    counter = counter + 1 

    return json.dumps({'counter' : counter, 'analysis': outputDictionary, 'image': im_b64}), 200

print('App loaded!')