import cv2
import pytesseract
from pytesseract import Output
import sys

def handle_mixed_document(image_path):
    # Load and convert to grayscale
    img = cv2.imread(image_path)
    img = cv2.resize(img, None, fx=5, fy=5, interpolation=cv2.INTER_CUBIC)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # image_to_data returns a dictionary with 'block_num', 'conf', and 'text'
    # This helps see where text exists versus where it's just visual noise
    data = pytesseract.image_to_data(gray, config=r'--oem 3 --psm 3',
                     output_type=Output.DICT)

    extracted_text_blocks = []
    
    n_boxes = len(data['text'])
    for i in range(n_boxes):
        # Filter: Only keep text with a confidence score > 60
        # Low confidence (< 0 or very low) often indicates an image or logo
        if int(data['conf'][i]) > 60:
            extracted_text_blocks.append(data['text'][i])
            
            # Optional: Draw boxes to see what was detected as text
            (x, y, w, h) = (data['left'][i], data['top'][i], data['width'][i], data['height'][i])
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

    # Save the visualized detection result
    cv2.imwrite('output/layout_detection.png', img)
    
    return " ".join(extracted_text_blocks)


if __name__ == "__main__":
    if len(sys.argv) > 1:
        book_img = sys.argv[1]
    else:
        book_img = "images/document_with_images.png"

    result = handle_mixed_document(book_img)
    print(result)

