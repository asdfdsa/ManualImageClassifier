# ManualImageClassifier
Manual image classifier for purposes such as deep learning

This is just a little piece of program that acts as a tool for conveniently classifying training images for purposes such as deep learning.

## ManualLabeler

Start GUI of the tool. Currently there are only three buttons: `class_1`, `class_2` and `skip`. Click on `class_1` if you want to classify the current image to the first class, and the program will copy the image to the corresponding folder. Same for `class_2`. Click on `skip` if you don't want to use the current image data. Next image will be shown as soon as you click on any of the three buttons.

Usage:

    ManualLabeler {arg1: path of an image folder with mixed-class image data} {arg2 (optional): particular file name that you are interested in, otherwise "*"} {arg3 (optional): particular folder name that is under arg1 and that you are interested in, otherwise "*"}

    e.g. ManualLabeler C:\images

## Requirements

 - Python3.7
 - matplotlib
 - numpy
 - shutil
