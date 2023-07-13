import requests
import os
import datetime
from datetime import datetime, timedelta

def her_vx(her1, her2, her3):
    compared ={her1:'', her2:'', her3:''}
    url = "https://akabab.github.io/superhero-api/api/all.json"
    heroes = requests.get(url).json()
    for heroi in heroes:
        for i in compared.keys():
            if heroi['name'] == i:
                compared[i] = heroi['powerstats']['intelligence']
    top = sorted(compared, key=compared.get, reverse=True)
    return print(f'Самый умный супергерой "{top[0]}"\n')
print('ЗД1:')
her_vx('Hulk', 'Captain America', 'Thanos')


class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def upload(self, file_path: str):
        """Метод загружает файлы по списку file_list на яндекс диск"""
        file_list = os.listdir(path_to_file)
        for name in file_list:
            url = "https://cloud-api.yandex.net/v1/disk/resources/upload"
            headers = {'Authorization': 'OAuth ' + token}
            param = {'path': '/uploaded_files/'+name}
            respons = requests.get(url, headers=headers, params=param)
            data = respons.json()
            if respons.status_code != 200:
               print(data['message'])
            else:
                url = data['href']
                with open(file_path+name, 'rb') as f:
                    requests.post(url, files={'file': f})
                    print('Файлы загружены')
        print('')

if __name__ == '__main__':
    print('ЗД2:')
    # Получить путь к загружаемому файлу и токен от пользователя
    path_to_file = 'C:\\Users\\rom.exe\\Documents\\in_ya.d\\'
    token = ""
    uploader = YaUploader(token)
    result = uploader.upload(path_to_file)


class questions:
    def __init__(self, tag):
        self.tag = tag

    def period(self, last_days):
        dt_now = datetime.today().strftime("%Y-%m-%d")
        d = (datetime.today() - timedelta(days=last_days)).strftime("%Y-%m-%d")
        url = "https://api.stackexchange.com/2.3/questions?order=desc&sort=activity&site=stackoverflow"
        param = {'fromdate': d, 'todate': dt_now, 'tagged': self.tag}
        respons = requests.get(url, params=param) #headers=headers, params=param
        data = respons.json()
        for i in data['items']:
            print(i['title'])
        return

if __name__ == '__main__':
    print('ЗД3:')
    que = questions('Python')
    result = que.period(2)