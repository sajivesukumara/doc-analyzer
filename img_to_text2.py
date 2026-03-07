import cv2
import ptesseract
from pytesseract import Output

def handle_mixed_document(image_path)
    # Load and convert to grayscale
    img = cv2.imread(image_path)
    gray = cv2.cvtColor(img, cv2.COLOR_BG2GRAY)

    #image_to_data returns a dictionary with block_num, conf and text 
    # This helps see where text exists versus where its just visual noise

    data = pytesseract.image_to_data(gray, output_type=Output.DICT)
    
    extracted_tet_blocks = []

    n_boxes = len(data['text']
    for i in range(n_boxes):
        # Filter: Only keep text with a confidence score > 60
        # Low confidence (<0 or very low) often indicates an image or logs
        if int(data['conf'][i]) > 60:
            extracted_text_blocks.append(data['text'][i])
            (x,y,w,h) = (data['left'][i], data['top'][i], data['width'][i], data['height'][i])
            cv2.rectangle(img, (x,y), (x_w, y+h), (0,255,0), 2)

   cv2.imwrite('output/layout_detection.png', img)
   return " ".join(extracted_text_blocks)

if __name__ == "__main__" :
    result = handle_mixed_document("images/document_with_images.png")
