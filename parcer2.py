import os
import requests
from label_studio_sdk import Client

# Настройки Label Studio
LS_ENDPOINT = "http://localhost:8080"
LS_API_KEY = "c7baac699eb7040104a351abe9b924451bcc3df1"

# Папки с изображениями
ORIGIN_FOLDER = "D:\\datasets\\dataset_3\\orig"
NOISY_FOLDER = "D:\\datasets\\dataset_3\\noisy"
OUTPUT_FOLDER = "C:\\Users\\Дима Титаренко\\Desktop\\Python\\prac3\\orig\\output"

# Создайте клиент Label Studio
client = Client(LS_ENDPOINT, LS_API_KEY)

# Создайте новый проект в Label Studio
project = client.create_project(name="Разметка зашумленных изображений")

# Пройдитесь по всем зашумленным изображениям
for filename in os.listdir(NOISY_FOLDER):
    if filename.endswith(".png"):
        noisy_image_path = os.path.join(NOISY_FOLDER, filename)
        text_file = os.path.join(OUTPUT_FOLDER, os.path.splitext(filename)[0] + ".txt")

        # Прочитайте текст из соответствующего текстового файла
        if os.path.isfile(text_file):
            with open(text_file, "r", encoding="utf-8") as f:
                text = f.read()
        else:
            print(f"Файл не найден: {text_file}")
            continue

        # Создайте задачу разметки в Label Studio
        task = {
            "image": noisy_image_path,
            "text_content": text
        }
        project.create_task(task)

print("Разметка зашумленных изображений завершена.")
