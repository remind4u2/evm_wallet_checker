import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

TIMEOUT = 8 # подбираем для себя комфортную задержку. На быстрых машинах достаточно 1 сек, и ногда надо и 10 сек

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
            url = f'https://zkswap.finance/zkflow?address={wallet}'
            
            driver.get(url)
            time.sleep(TIMEOUT) 

            # Wait for the element with class "mui-hx4d9l" to appear (timeout after 10 seconds)
            div_elements = WebDriverWait(driver, 10).until(
                EC.presence_of_all_elements_located((By.XPATH, '//div[@font-size="3rem" and @font-weight="800" and @color="#2363eb" and @lineheight="1" and @mb="8px"]'))
            )
            wallet_info = ""  
            # Extract text from each div
            for div_element in div_elements:
                # Extract text from the div
                if div_element:
                    text = div_element.text
                    # Extract the number using regex
                    import re
                    number = re.search(r'\d+', text)
                    if number:
                        
                        wallet_info = wallet_info +";"+ number.group()
                    else:
                        print("No number found in the div.")
                else:
                    print("Div element not found.")

            print(f"{wallet};{wallet_info}")
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