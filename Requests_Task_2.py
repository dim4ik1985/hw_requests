import requests


class YaUploader:
    host = 'https://cloud-api.yandex.net:443'

    def __init__(self, token: str):
        self.token = token

    def upload(self, file_path: str):
        """Метод загружает файлы по списку file_list на яндекс диск"""
        url = f'{self.host}/v1/disk/resources/upload'
        params = {'path': file_path, 'overwrite': True}
        headers = {'Content-Type': 'application/json', 'Authorization': f'OAuth {self.token}'}
        request_href = (requests.get(url, params=params, headers=headers)).json().get('href')
        requests.put(request_href, data=open(file_path, 'rb'), headers=headers)


if __name__ == '__main__':
    # Получить путь к загружаемому файлу и токен от пользователя
    path_to_file = 'F.P.G-Mom_I_canT_drink_more.mp3'
    token = ''
    uploader = YaUploader(token)
    result = uploader.upload(path_to_file)
