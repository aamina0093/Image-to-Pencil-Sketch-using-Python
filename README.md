# Image to Pencil Sketch using Python

**Description:**
The program converts the given image to a pencil sketch using open-cv module in python.

**Procedure:**
1. After importing the module and reading the image, convert the image into a grayscale mode. 
2. For enhancing details of the image we get the negative image of the grayscale image.
3. Then we blur the negative image and then invert it again.
4. Now we get a pencil sketch image by mixing grayscale image with the blurred inverted image.

**Language Used:**
Python (v-3.9.9)

**Tools Used:**
Pycharm (v-2021.1.3)
