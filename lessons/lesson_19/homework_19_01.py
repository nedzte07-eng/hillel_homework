import os
import requests

def picture_save(picture_href):

    save_dir = "NASA_backup"
    os.makedirs(save_dir, exist_ok=True)

    filename = os.path.join(save_dir, os.path.basename(picture_href))

    response2 = requests.get(picture_href)
    response2.raise_for_status()

    with open(filename, "wb") as f:
        f.write(response2.content)


BASE_URL = "https://images-api.nasa.gov"

# Пошук зображень
search_url = f"{BASE_URL}/search"
search_params = {
    "q": "Curiosity rover Mars",  # пошуковий запит
    "media_type": "image",  # тільки зображення
    "page_size": 20  # щоб було з чого вибрати
}

# # Отримання файлів по nasa_id
# asset_url_template = f"{BASE_URL}/asset/{{nasa_id}}"

response = requests.get(search_url, params=search_params)


if response.status_code == 200:
    data = response.json()['collection']['items']

    first_id = data[0]["data"][0]['nasa_id']
    first_picture = requests.get(f'{BASE_URL}/asset/{first_id}')
    pictures_urls = first_picture.json()['collection']['items']
    picture1_href = pictures_urls[0]['href']

    second_id = data[1]["data"][0]['nasa_id']
    second_picture = requests.get(f'{BASE_URL}/asset/{second_id}')
    pictures_urls = second_picture.json()['collection']['items']
    picture2_href = pictures_urls[0]['href']

    picture_save(picture1_href)
    picture_save(picture2_href)


else:
    print('Bad connection')