import cv2
import pytesseract

# Path to Tesseract executable (change this based on your system configuration)
pytesseract.pytesseract.tesseract_cmd = r'"C:\Users\dhi29\PycharmProjects\planlearningpython\pytesseract pillow gTTS"'

def extract_text_from_image(image_path):
    # Read the image
    img = cv2.imread(image_path)

    # Convert the image to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Use Tesseract OCR to extract text from the image
    extracted_text = pytesseract.image_to_string(gray)

    return extracted_text

# Path to the input image containing handwritten text
image_path = 'text.jpg'

# Extract text from the image
extracted_text = extract_text_from_image(image_path)

# Print the extracted text
print("Extracted Text:")
print(extracted_text)
