from web3 import Web3

# Сети:      
# ETH, ZKSYNC, SCROLL, BASE, LINEA, ZKF, MANTA, ARBITRUM, OP, NOVA, ZORA, BSC, FTM, AVAXC, MATIC, CORE, CELO, METIS, HARMONY, GNOSIS
# для ZORA нужен vpn в РФ и РБ
CHAIN = 'ZKSYNC'        
DELIMETR = ';'        # разделитель, можете использовать свой, например ' | ' или ' ' или '-'
SHOW_TOKEN = False     # если True то в конце суммы, на каждой стрке выводит валюту токена , наприме ETH или USDC

RPCS = [
    {'chain': 'ETH',        'rpc': 'https://rpc.ankr.com/eth',               'scan': 'https://etherscan.io',                'token': 'ETH'},
    {'chain': 'ZKSYNC',     'rpc': 'https://rpc.ankr.com/zksync_era',        'scan': 'https://www.oklink.com/zksync',       'token': 'ETH'},
    {'chain': 'ARBITRUM',   'rpc': 'https://arb1.arbitrum.io/rpc',           'scan': 'https://arbiscan.io',                 'token': 'ETH'},
    {'chain': 'NOVA',       'rpc': 'https://rpc.ankr.com/arbitrumnova',      'scan': 'https://nova.arbiscan.io',            'token': 'ETH'},
    {'chain': 'OPTIMISM',   'rpc': 'https://rpc.ankr.com/optimism',          'scan': 'https://optimistic.etherscan.io',     'token': 'ETH'},
    {'chain': 'SCROLL',     'rpc': 'https://rpc.ankr.com/scroll',            'scan': 'https://scrollscan.com',              'token': 'ETH'},
    {'chain': 'BASE',       'rpc': 'https://1rpc.io/base',                   'scan': 'https://basescan.org',                'token': 'ETH'},
    {'chain': 'LINEA',      'rpc': 'https://1rpc.io/linea',                  'scan': 'https://lineascan.build',             'token': 'ETH'},
    {'chain': 'MANTA',      'rpc': 'https://1rpc.io/manta',               'scan': 'https://pacific-explorer.manta.network/','token': 'ETH'},
    {'chain': 'ZORA',       'rpc': 'https://rpc.zora.energy',                'scan': 'https://explorer.zora.energy/',       'token': 'ETH'},
    {'chain': 'ZKF',        'rpc': 'https://rpc.zkfair.io',                  'scan': 'https://scan.zkfair.io',              'token': 'USDC'},
    {'chain': 'BSC',        'rpc': 'https://rpc.ankr.com/bsc',               'scan': 'https://bscscan.com',                 'token': 'BNB'},
    {'chain': 'MATIC',      'rpc': 'https://rpc.ankr.com/polygon',           'scan': 'https://polygonscan.com',             'token': 'MATIC'},
    {'chain': 'AVAXC',      'rpc': 'https://avalanche.public-rpc.com',       'scan': 'https://snowtrace.io',                'token': 'AVAX'},
    {'chain': 'FTM',        'rpc': 'https://rpc.ankr.com/fantom',            'scan': 'https://ftmscan.com',                 'token': 'FTM'},
    {'chain': 'CORE',       'rpc': 'https://rpc.coredao.org',                'scan': 'https://scan.coredao.org',            'token': 'CORE'},
    {'chain': 'METIS',      'rpc': 'https://andromeda.metis.io/?owner=1088', 'scan': 'https://andromeda-explorer.metis.io', 'token': 'METIS'},
    {'chain': 'GNOSIS',     'rpc': 'https://rpc.ankr.com/gnosis',            'scan': 'https://gnosisscan.io',               'token': 'XDAI'},
    {'chain': 'CELO',       'rpc': 'https://rpc.ankr.com/celo',              'scan': 'https://celoscan.io',                 'token': 'CELO'},
    {'chain': 'HARMONY',    'rpc': 'https://rpc.ankr.com/harmony',           'scan': 'https://explorer.harmony.one',        'token': 'ONE'},
    {'chain': 'ZKEVM',      'rpc': 'https://1rpc.io/polygon/zkevm',          'scan': 'https://zkevm.polygonscan.com/',      'token': 'ETH'},
]

def check_rpc(chain):
    for elem in RPCS:
        if elem['chain'] == chain:
            RPC = elem['rpc']
            scan = elem['scan']
            token = elem['token']

            return {
                'rpc': RPC, 'scan': scan, 'token': token
            }

if __name__ == "__main__":
    with open("wallets.txt", "r") as f:
        WALLETS = [row.strip() for row in f]

    if (len(WALLETS) > 0):
    
        rpc = check_rpc(CHAIN)['rpc']
        token = check_rpc(CHAIN)['token']
        web3 = Web3(Web3.HTTPProvider(rpc))
        total = 0
        total_tx = 0
        print(f'Начинаем проверку кошельков в сети: {CHAIN}:')
        print()
        print(f'---------------------------------------------------------')
        print(f'| кошелек                                   |транз |бал |')
        print(f'---------------------------------------------------------')
        for wallet in WALLETS:
            wallet  = Web3.to_checksum_address(wallet)
            nonce = web3.eth.get_transaction_count(wallet)
            balance = web3.eth.get_balance(wallet)
            balance = round(Web3.from_wei(balance, 'ether'), 6)
            total = total + balance
            total_tx = total_tx + nonce
            result = f'{wallet}{DELIMETR}{nonce}{DELIMETR}{balance}'
            if (SHOW_TOKEN):
                result = f'{result} {token}'
            print(result)

        tx_average = round(total_tx/len(WALLETS))
        print(f'---------------------------------------------------------')
        print()
        print(f'Суммарный баланс: {total} {token} в сети {CHAIN}')
        print(f'Среднее кол-во транзакций на кошелек: {tx_average}')

    else:
        print()
        print()
        print(f'Файл wallets.txt пустой!!! Впишите туда адреса кошельков, котрые хотите проверить.')
    print()
    print()
    print(f'https://t.me/slow_rich | Ты получишь мега иксы в 2024 году. Да, да, именно ты! | https://t.me/slow_rich')
    print(f'https://t.me/slow_rich | Ты получишь мега иксы в 2024 году. Да, да, именно ты! | https://t.me/slow_rich')
    print(f'https://t.me/slow_rich | Ты получишь мега иксы в 2024 году. Да, да, именно ты! | https://t.me/slow_rich')