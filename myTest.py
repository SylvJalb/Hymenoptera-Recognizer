import yolov5

# load pretrained model
model = yolov5.load('./models/yolov5m_v2.pt')
  
# set model parameters
model.conf = 0.25  # NMS confidence threshold
model.iou = 0.45  # NMS IoU threshold
model.agnostic = False  # NMS class-agnostic
model.multi_label = False  # NMS multiple labels per box
model.max_det = 20  # maximum number of detections per image

print("end load!")



# set image
img = 'C:/Users/Marco/________VS Code/Progetti VS Code/Hymenoptera-Recognizer/src/image_1.jpg'
img1 = 'C:/Users/Marco/________VS Code/Progetti VS Code/Hymenoptera-Recognizer/src/image_1.jpeg'

# perform inference
results1 = model(img)
results = model(img1)


# parse results
predictions = results.pred[0]
boxes = predictions[:, :4] # x1, y1, x2, y2
scores = predictions[:, 4]
categories = predictions[:, 5]


for index, cat in enumerate(categories):
    output = ""
    if 0. in cat:
        output = "Ape"      #rosso
    if 1. in cat:
        output = "Vespa"        #rosa
    if 2. in cat:
        output = "Calabrone Europeo"    #arancio scuro
    if 3. in cat:
        output = "Vespa Orientale"      #arancio chiaro
    if 4. in cat:
        output = "Velutina (Calabrone Asiatico)"    #giallo



#'FF3838', 'FF9D97', 'FF701F', 'FFB21D', 'CFD231'

    print(output + " " + str(scores[index])[7:14])

# show detection bounding boxes on image
results.show()

# save results into "results/" folder
results.save(save_dir='resultsMyTest/')


