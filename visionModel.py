import torch
import pandas
import numpy as np

# Model
#model = torch.hub.load('ultralytics/yolov5', 'yolov5s')  # or yolov5m, yolov5l, yolov5x, etc.
model = torch.hub.load('ultralytics/yolov5', 'custom', 'best.pt')  # custom trained model

# Images
def doVision(im):
    #im = '/Users/ryan/Desktop/ECE477/Code/real.jpg'  # or file, Path, URL, PIL, OpenCV, numpy, list
    # Inference
    results = model(im)
    # Results
    # results.print()  # or .show(), .save(), .crop(), .pandas(), etc.
    # results.xyxy[0]  # im predictions (tensor)
    # results.pandas().xyxy[0]  # im predictions (pandas)
    re = results.pandas().xyxy #list
    cardsList = re[0]['name'].values.tolist()

    return cardsList
#      xmin    ymin    xmax   ymax  confidence  class    name
# 0  749.50   43.50  1148.0  704.5    0.874023      0  person
# 2  114.75  195.75  1095.0  708.0    0.624512      0  person
# 3  986.00  304.00  1028.0  420.0    0.286865     27     tie
