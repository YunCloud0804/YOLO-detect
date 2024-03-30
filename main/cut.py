# -*- coding: utf-8 -*-
"""
Created on Sun Dec 13 21:49:55 2020

@author: YaoYee
"""

import cv2
import os
import math
# Cutting the input image to h*w blocks
#heightCutNum = 3;
#widthCutNum = 1;

# The folder path of input and output
inPath = "C:/Users/Cloud/Desktop/TEST_SCH/"
outPath = "C:/Users/Cloud/Desktop/test-cut-sch/"

for f in os.listdir(inPath):

    path = inPath + f.strip()
    print(path)
    img = cv2.imread(path)

    # The size of each input image
    height = img.shape[0]
    width = img.shape[1]

    # The size of block that you want to cut
    heightBlock = 512
    widthBlock = 512
    heightCutNum = math.ceil(height / heightBlock)
    widthCutNum  = math.ceil(height / widthBlock)
    for i in range(0, heightCutNum):
        for j in range(0, widthCutNum):
            cutImage = img[i * heightBlock:(i + 1) * heightBlock, j * widthBlock:(j + 1) * widthBlock]
            savePath = outPath + f.strip()[0:5] + "_" + str(i) + ".jpg"
            cv2.imwrite(savePath, cutImage)

