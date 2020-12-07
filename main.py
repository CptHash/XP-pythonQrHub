#!/usr/bin/env python3
from qrtools import QR
import re
import os
import sys
import cv2

def video_reader():
    cam = cv2.VideoCapture(0)
    detector = cv2.QRCodeDetector()
    
    while True:
        _, img = cam.read()
        data, bbox, _ = detector.detectAndDecode(img)
        if data:
            password = re.findall("P:(.*?);;", data)[0]
            print(password)
            cam.release()
            cv2.destroyAllWindows()
            break
        cv2.imshow("img", img)
        if cv2.waitKey(1) == ord("Q"):
            break
    cam.release()
    cv2.destroyAllWindows()

def qr_generator(value):
    my_QR = QR(data=value)
    my_QR.encode()
    cmd = 'mv ' +  my_QR.filename + ' ./generated_qr/qr.jpg'
    os.system(cmd)
    print("qr.jpg generated for password: \"" + value + "\"")

def generateFromFile():
    my_QR = QR(filename="/home/mathieu/Epitech/xp_qrcode/qr.jpg")

    if (my_QR.decode() == True):
        print ("OK")


if __name__ == '__main__':
    args = []
    
    for arg in sys.argv:
        args.append(arg)
    if (len(args) == 1):
        print ("Usage: ./main.py [reader:generator:remaker] value")
        exit(84)
    if (args[1] == "reader"):
        video_reader()
    elif (args[1] == "generator"):
        if (len(args) == 3):
            qr_generator(args[2])
        else:
            print("Parameter \"value\" is missing !")
            print ("Usage: ./main.py generator value")
