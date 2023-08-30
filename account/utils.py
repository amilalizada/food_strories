import requests
import os
from food import settings

def download_image(url):

    response = requests.get(url)
    print(settings.MEDIA_ROOT)
    file_name = 'profile_images/'  + url.split('/')[-1]  + '.png'
    file_path = os.path.join(settings.MEDIA_ROOT , file_name)
    print(file_path)
    with open(file_path, 'wb') as f:
        f.write(response.content)

    return file_name


