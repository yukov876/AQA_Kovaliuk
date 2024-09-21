import requests

base_url = 'http://127.0.0.1:8080'

image_path = 'C:\\Users\\-Admin-\\PycharmProjects\\AQA_Kovaliuk\\lesson_19\\homework_19_2\\uploads\\image.jpg'  # Вкажіть шлях до вашого зображення
with open(image_path, 'rb') as img_file:
    files = {'image': img_file}
    response = requests.post(f'{base_url}/upload', files=files)

if response.status_code == 201:
    response_data = response.json()
    image_url = response_data.get('image_url')

    result = {
        "status_code": response.status_code,
        "image_url": image_url
    }
    print(result)


filename = image_url.split('/')[-1]
response = requests.get(f'{base_url}/uploads/{filename}')
if response.status_code == 200:
    with open(f'downloaded_{filename}', 'wb') as f:
        f.write(response.content)
    print(f'Зображення завантажено локально як downloaded_{filename}')
else:
    print(f'Не вдалося отримати зображення: {response.status_code}')

response = requests.delete(f'{base_url}/delete/{filename}')

if response.status_code == 200:
    print(response.json())
else:
    print(f'Помилка видалення: {response.status_code}')
