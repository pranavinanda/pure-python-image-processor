Pure Python Image Processor

Overview-
This project implements basic grayscale image processing operations using core Python. The image is represented as a two-dimensional list of pixel values ranging from 0 to 255.

Features-
Invert Image: Reverses pixel values using 255 - pixel
Adjust Brightness: Increases or decreases brightness while keeping values between 0 and 255
Thresholding: Converts grayscale pixels into black or white based on a threshold
Horizontal Flip: Reverses pixels in each row
Vertical Flip: Reverses the order of rows
Rotate Image: Rotates the image 90 degrees clockwise
Crop Image: Extracts a selected section of the image
Blur Image: Averages neighbouring pixels to create a blur effect
Display Image: Prints the image row by row

Technologies Used-
Python 3
Core Python: lists, loops, functions, conditionals, and arithmetic operations.

How to Run-
Install Python 3.
Open the project folder in a terminal.
Run: python image_processor.py

Image Representation-
The image is stored as a two-dimensional list. Each number represents a grayscale pixel intensity between 0 (black) and 255 (white).

Limitations-
The program uses pixel values stored in a Python list.
It does not currently load or save standard image files such as PNG or JPEG.
Blur averages the available neighbouring pixels.

Conclusion-
This project demonstrates basic image processing operations using core Python without external image processing libraries.

