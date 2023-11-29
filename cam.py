import cv2 as cv

def takePic():
    cam = cv.VideoCapture(0) 
    result, image = cam.read() 
    return result, image
