import requests
import json
from fake_useragent import UserAgent


if __name__ == "__main__":
    with open("wallets.txt", "r") as f:
        WALLETS = [row.strip() for row in f]

    if (len(WALLETS) > 0):
        print()
        print(f'Начинаем проверку кошельков на наличие POH:')
        print()
        print(f'------------------------------------------------')
        print(f'| кошелек                              |POH    |')
        print(f'------------------------------------------------')

        for wallet in WALLETS:
            # Fetch the HTML content of the webpage
            url = f'https://linea-xp-poh-api.linea.build/poh/{wallet}'

            headers ={
                'User-Agent':UserAgent().random,
                'method':f'GET',
            }

            resp = requests.get(url, headers=headers)
            if resp.status_code == 200:
        
                    text = json.loads(resp.text)
                    poh = text['poh']
                    if (poh == False):
                        print(f'{wallet};{poh}')

        print(f'------------------------------------------------')