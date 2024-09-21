import requests

url = 'https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos'
params = {
    'sol': 1000,
    'camera': 'fhaz',
    'api_key': 'DEMO_KEY'
}

response = requests.get(url, params=params)

if response.status_code == 200:
    data = response.json()

    for i, photo in enumerate(data['photos'][:2], start=1):
        img_url = photo['img_src']
        img_response = requests.get(img_url)

        file_name = f'mars_photo{i}.jpg'
        with open(file_name, 'wb') as f:
            f.write(img_response.content)
        print(f'Фото {file_name} збережено успішно!')
else:
    print(f'Запит не успішний. Код помилки: {response.status_code}')
