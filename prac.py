# import pytesseract
# from PIL import Image
# img = Image.open('ORIG_1 (Zara Larsson album) - Wikipedia_20240327T120158.943406_.png')
# pytesseract.pytesseract.tesseract_cmd = r'D:\tesseract\tesseract.exe'
# custom_config = r'--oem3 --psm13'

# text = pytesseract.image_to_string(img, config=custom_config)
# print(text)

import pytesseract
from PIL import Image
img = Image.open('C:\\Users\\Дима Титаренко\\Desktop\\Python\\prac3\\ORIG_1 (Zara Larsson album) - Wikipedia_20240327T120158.943406_.png')

pytesseract.pytesseract.tesseract_cmd = r'D:\tesseract\tesseract.exe'
custom_config = r'--oem 3 --psm 3'


text = pytesseract.image_to_string(img, config=custom_config)
print(text)

with open('C:\\Users\\Дима Титаренко\\Desktop\\Python\\prac3\\ORIG_1 (Zara Larsson album) - Wikipedia_20240327T120158.943406_.png', 'w') as text_file:
    text_file.write(text)
