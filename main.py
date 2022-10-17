import requests
from pprint import pprint

# Задание 1
link = 'https://cdn.jsdelivr.net/gh/akabab/superhero-api@0.3.0/api/all.json'
response1 = requests.get(link)

hero_dict = {}
for hero in response1.json():
    if hero['name'] == 'Hulk' or hero['name'] == 'Captain America' or hero['name'] == 'Thanos':
        hero_dict[hero['name']] = hero['powerstats']['intelligence']
    else:
        continue

print(f'Самым умным из героев (Hulk, Captain America, Thanos) является {max(hero_dict)},'
      f' интеллект которого равен {max(hero_dict.values())}.')


# Задание  2
class YandexDisk:
    def __init__(self, token):
        self.token = token

    def get_headers(self):
        return {
            'Content-Type': 'application/json',
            'Authorization': f'OAuth {self.token}'
        }

    def get_files_list(self):
        files_url = 'https://cloud-api.yandex.net/v1/disk/resources/files'
        headers = self.get_headers()
        response = requests.get(files_url, headers=headers)
        return response.json()

    def _get_upload_link(self, disk_file_path):
        upload_url = "https://cloud-api.yandex.net/v1/disk/resources/upload"
        headers = self.get_headers()
        params = {"path": disk_file_path, "overwrite": "true"}
        response = requests.get(upload_url, headers=headers, params=params)
        pprint(response.json())
        return response.json()

    def upload_file_to_disk(self, disk_file_path, filename):
        result = self._get_upload_link(disk_file_path=disk_file_path)
        href = result.get('href', '')
        response = requests.put(href, data=open(filename, 'rb'))
        response.raise_for_status()
        if response.status_code == 201:
            print("Success")

if __name__ == '__main__':
    token = "___________________" #сюда копируется токен с полигона яндекса, чтобы загрузить/скачать файлы
    ya = YandexDisk(token)
    ya.upload_file_to_disk('test.txt', r'C:\Users\Андрей\Desktop\hw8\test.txt')