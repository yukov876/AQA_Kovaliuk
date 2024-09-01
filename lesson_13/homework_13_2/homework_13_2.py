import json
import logging
import os
from pathlib import Path

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler('json_kovaliuk.txt')
file_handler.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)

parent_dir = Path('C:\\Users\\-Admin-\\PycharmProjects\\AQA_Kovaliuk\\lesson_13\\homework_13_2')

extension = '.json'
json_file = [f for f in os.listdir(parent_dir) if f.endswith(extension)]
for file in json_file:
    try:
        data = json.loads(file)
        print(f'Файл {file} у вірному форматі json')
    except json.JSONDecodeError as e:
        logger.error(f"Помилка розбору JSON у файлі {file}")
        