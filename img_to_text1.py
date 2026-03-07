import cv2
import pytesseract
from PIL import Image
import os

# 1. WINDOWS ONLY: Point to your Tesseract executable
# pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def perform_ocr(image_path):
    # Load the image using OpenCV
    image = cv2.imread(image_path)
    
    # Preprocessing: Convert to grayscale for better results
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Optional: Apply thresholding to create a binary image
    # _, threshold_img = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
    
    # Use Tesseract to convert image to string
    extracted_text = pytesseract.image_to_string(gray)
    
    return extracted_text

if __name__ == "__main__":
    img_name = "sample_text.png"
    img_path = os.path.join("images", img_name)
    
    if os.path.exists(img_path):
        print(f"--- Extracting text from {img_name} ---")
        result = perform_ocr(img_path)
        print(result)
        
        # Save to output folder
        with open("output/result.txt", "w") as f:
            f.write(result)
    else:
        print(f"Error: Image not found at {img_path}")
