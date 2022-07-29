import requests
import os
from pprint import pprint
token = ''

class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def upload(self, file_path: str):
        # """Метод загружает файлы по списку file_list на яндекс диск"""
        file_url = 'https://cloud-api.yandex.net/v1/disk/resources/upload'
        headers = {'Content-Type': 'application/json', 'Authorization': f'OAuth {token}'}
        params = {'path': file_path, 'overwrite': 'true'}
        response = requests.get(file_url, headers=headers, params=params).json()
        href = response.get('href', '')
        res = requests.put(href, data=open(file_path, 'rb'))
        if res.status_code == 201:
            return 'Загрузка прошла успешно!'
        else:
            return f'Ошибка загрузки! Код ошибки: {res.status_code}'


if __name__ == '__main__':
    # Получить путь к загружаемому файлу и токен от пользователя
    path_to_file = 'file.txt'
    token = token
    uploader = YaUploader(token)
    result = uploader.upload(path_to_file)