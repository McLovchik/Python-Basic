import requests
import json

info = requests.get('https://www.breakingbadapi.com/api/deaths')
if info.status_code == 200:
    data = json.loads(info.text)
    max_deaths = max(data[x_episode]['number_of_deaths'] for x_episode in range(len(data)))
    for i_episode in range(len(data)):
        if data[i_episode]['number_of_deaths'] == max_deaths:
            with open('info_deaths.json', 'w') as file_info_deaths:
                json.dump(data[i_episode], file_info_deaths, indent=4)
            print('ID эпизода:', data[i_episode]['death_id'])
            print('Номер сезона:', data[i_episode]['season'])
            print('Номер эпизода:', data[i_episode]['episode'])
            print('Общее количество смертей:', max_deaths)
            break
