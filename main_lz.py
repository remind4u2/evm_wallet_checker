import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

TIMEOUT = 5 # подбираем для себя комфортную задержку. На быстрых машинах достаточно 1 сек, и ногда надо и 10 сек

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
        print(f'Начинаем проверку кошельков в layerzeroscan:')
        print()
        print(f'------------------------------------------------')
        print(f'| кошелек                              |транз  |')
        print(f'------------------------------------------------')
        total_tx = 0
        for wallet in WALLETS:
            # Fetch the HTML content of the webpage
            url = f'https://layerzeroscan.com/address/{wallet}'
            
            driver.get(url)
            time.sleep(TIMEOUT) 

            # Wait for the element with class "mui-hx4d9l" to appear (timeout after 10 seconds)
            total_messages_span = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.CLASS_NAME, 'mui-hx4d9l'))
                )
                
            # Extract text from the span
            total_messages = total_messages_span.text
            if (total_messages == '-'):
                total_messages = 0
            total_tx = total_tx + int(total_messages)
            print(f"{wallet};{total_messages}")

        tx_average = round(total_tx/len(WALLETS))
        driver.quit()
        print(f'------------------------------------------------')
        print()
        print(f'Всего проверено {len(WALLETS)} кошельков')
        print(f'Среднее кол-во транзакций на кошелек: {tx_average}')
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