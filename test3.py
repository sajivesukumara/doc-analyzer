import sys
import cv2
import pytesseract
import numpy as np

def clean_vintage_page(image_path):
    # 1. Load image
    img = cv2.imread(image_path)
    
    # 2. Rescale: Make the image 2x larger to help with thin serif fonts
    img = cv2.resize(img, None, fx=2, fy=2, interpolation=cv2.INTER_CUBIC)
    
    # 3. Convert to Grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    # 4. Adaptive Thresholding: This is CRITICAL for the yellowed background. 
    # It calculates thresholds for small pixel neighborhoods to handle uneven lighting.
    cleaned = cv2.adaptiveThreshold(
        gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2
    )

    # 5. Denoise: Remove small dots/paper texture specks
    kernel = np.ones((1, 1), np.uint8)
    cleaned = cv2.dilate(cleaned, kernel, iterations=1)
    cleaned = cv2.erode(cleaned, kernel, iterations=1)

    # 6. OCR with Custom Config
    # --psm 3: Automatic page segmentation (handles text wrapping)
    # --oem 3: Default OCR Engine Mode (LSTM)
    custom_config = r'--oem 3 --psm 3'
    text = pytesseract.image_to_string(cleaned, config=custom_config)
    
    return text

if __name__ == "__main__":
   if len(sys.argv) > 1:
      book_img = sys.argv[1]
   else: 
      book_img = "images/raggedy_ann.jpg"

   print(clean_vintage_page(book_img))

