import requests

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