import os
import pytesseract
from PIL import Image

# Установите путь к Tesseract
pytesseract.pytesseract.tesseract_cmd = r'D:\tesseract\tesseract.exe'

# Укажите папку с изображениями
image_folder = 'C:\\Users\\Дима Титаренко\\Desktop\\Python\\prac3\\orig'

# Создайте папку для сохранения результатов
output_folder = os.path.join(image_folder, 'output')
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Обработка всех изображений в папке
for filename in os.listdir(image_folder):
    if filename.endswith('.png'):
        image_path = os.path.join(image_folder, filename)
        img = Image.open(image_path)

        custom_config = r'--oem 3 --psm 3'
        text = pytesseract.image_to_string(img, config=custom_config)

        # Сохранение результата в текстовый файл
        output_file = os.path.join(output_folder, os.path.splitext(filename)[0] + '.txt')
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(text)

        print(f'Обработано изображение: {filename}')
