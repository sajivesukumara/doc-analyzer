# doc-analyzer
An OCR (Optical Character Recognition) based project to read printed documents

## Prerequisites

Install Tesseract engine on your operating system before running the code

* Windows : Donwload and run teh officiall installer.
* macOS: Use Homebrew: ```brew install tesseract-ocr```
* Linux: Run ```sudo apt install tesseract-ocr```

Next, install the required Python libraries
```
pip install pytesseract opencv-python Pillow
```

docker pull docker.io/library/python:3.11-slim-bullseye
docker run -it -v /Users/sajisuku/tmp:/experiments1 localhost/ocr_image_1 bash


## Tips for Success

**Image quality** : Works best with high-resolution, clear and orizontally aligned text <br>
**Preprocessing** : If results are poor, try resizing the image or using OpenCV to remove noise and enhance contrast <br>
**Page Segmentation** : For complex layout, use custom configurations like --psm 6
