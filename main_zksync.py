import time
from web3 import Web3
import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

TIMEOUT = 3 # подбираем для себя комфортную задержку. На быстрых машинах достаточно 1 сек, и ногда надо и 10 сек
rpcs = [
    # 'https://1rpc.io/zksync2-era', 
    'https://mainnet.era.zksync.io', 
    # 'https://zksync-era.blockpi.network/v1/rpc/public', 
    # 'https://zksync.meowrpc.com'
    ]

if __name__ == "__main__":
    with open("wallets.txt", "r") as f:
        WALLETS = [row.strip() for row in f]

    if (len(WALLETS) > 0):

        options = webdriver.ChromeOptions()
        options.add_argument('--headless')
        options.add_argument('--no-sandbox')  
        options.add_argument('--disable-dev-shm-usage')

        # Initialize the WebDriver with the provided Chrome driver path and options
        driver = webdriver.Chrome(options=options)
        print()
        print(f'Начинаем проверку кошельков в zkflow')
        print(f'Формат:')
        print(f'Адрес; количество транз; баланс ETH; объем $; комиссии $; месяцы; недели; дни')
        print()
        print(f' ---------------------------------------------------------------------')
        print(f'| кошелек                                 |тр|баланс|объем|комс|м|н|д|')
        print(f' ---------------------------------------------------------------------')
        total_tx = 0
        for wallet in WALLETS:
            # Fetch the HTML content of the webpage
            url = f'https://zkswap.finance/zkflow?address={wallet}'
            
            driver.get(url)
            time.sleep(TIMEOUT) 

            rpc = random.choice(rpcs)
            web3 = Web3(Web3.HTTPProvider(rpc))

            wallet  = Web3.to_checksum_address(wallet)
            nonce = web3.eth.get_transaction_count(wallet)
            balance = web3.eth.get_balance(wallet)
            balance = round(Web3.from_wei(balance, 'ether'), 5)

            # Wait for the element with class "mui-hx4d9l" to appear (timeout after 10 seconds)
            div_elements = WebDriverWait(driver, 10).until(
                EC.presence_of_all_elements_located((By.XPATH, '//div[@font-size="3rem" and @font-weight="800" and @color="#2363eb" and @lineheight="1" and @mb="8px"]'))
            )
            wallet_info = ""  
            # Extract text from each div
            i = 1
            for div_element in div_elements:
                # Extract text from the div
                if (i > 1) :
                    if div_element:
                        text = div_element.text
                        # Extract the number using regex
                        import re
                        number = re.search(r'\d+', text)
                        if number:
                            wallet_info = wallet_info +";"+ number.group()
                        else:
                            wallet_info = wallet_info +";0"
                    else:
                        print("Div element not found.")
                i = i + 1

            import re
            # Wait for the element with class "mui-hx4d9l" to appear (timeout after 10 seconds)
            div_elements = WebDriverWait(driver, 10).until(
                EC.presence_of_all_elements_located((By.XPATH, '//div[@font-weight="600" and @font-size="14px" and @color="text"]')) or EC.presence_of_all_elements_located((By.XPATH, '//div[@font-size="14px" and @font-weight="600" and @color="text"]'))
            )

            # print(f'div_elements size = {len(div_elements)}')

            if (len(div_elements) == 14):
                # Extract text from each div
                day_element = div_elements[9].text
                days = re.search(r'\d+', day_element).group()

                week_element = div_elements[11].text
                weeks = re.search(r'\d+', week_element).group()

                month_element = div_elements[13].text
                months = re.search(r'\d+', month_element).group()
            
            if (len(div_elements) == 13):
                # Extract text from each div
                day_element = div_elements[8].text
                days = re.search(r'\d+', day_element).group()

                week_element = div_elements[10].text
                weeks = re.search(r'\d+', week_element).group()

                month_element = div_elements[12].text
                months = re.search(r'\d+', month_element).group()

            print(f"{wallet};{nonce};{balance}{wallet_info};{months};{weeks};{days}")
        driver.quit()
        print(f' ---------------------------------------------------------------------')
        print()
        print(f'Всего проверено {len(WALLETS)} кошельков')
        print()

    else:
        print()
        print(f'----------------------------------------------------------------------------------')
        print(f'Файл wallets.txt пустой!!! Впишите туда адреса кошельков, котрые хотите проверить.')
        print(f'----------------------------------------------------------------------------------')
        print()
    print(f'https://t.me/slow_rich | Подпишись на канал, и станешь миллиардером | https://t.me/slow_rich')
    print(f'https://t.me/slow_rich | Подпишись на канал, и станешь миллиардером | https://t.me/slow_rich')
    print(f'https://t.me/slow_rich | Подпишись на канал, и станешь миллиардером | https://t.me/slow_rich')