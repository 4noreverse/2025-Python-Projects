import json #fetch price data, http get requests
import requests #store and load data from ports
import os #gonna be used for file not found
COIN_IDS = {
    'btc':'bitcoin',
    'eth':'ethereum',
    'sol':'solana',
    'xrp':'ripple',
    'ada':'cardano',
    'hbar':'hedera',
    'dot':'polkadot',
    'doge':'dogecoin',
    'usdt':'tether',
    'ltc':'litecoin',
    'link':'chainlink',
    'uni':'uniswap',
    'fort':'forta'
}
# uzi flow program starts to main() then show menu -> user ticker -> call of the functions for port, price and calc -> return to menu -> exit
def main(): #menu and user input
    port = load()

    while True:
        print('Port Analyzer 3000')
        print('1 - View port')
        print('2 - Add to port')
        print('3 - Quit')
        dec = input('Choose an option (1,2,3): ').strip()

        if dec == '1':
            display_port(port)
        elif dec == '2':
            crypto(port)
        elif dec == '3':
            save(port)
            print('Thank You for choosing my program !')
            break
        else:
            print('Invalid')
def crypto(port):# add to the port
    print('Supported Currencies: ', ', '.join(COIN_IDS.keys()))
    tick = input('Enter the ticker of the coin to be purchased: ').strip().lower()
    if tick not in COIN_IDS:
        print('Unsupported')
        return
    quant = clean_quant()
    if tick in port:
        port[tick] = port[tick] + quant
        print(f'Added more {tick.upper()}')
    else:
        port[tick] = quant
        print(f'Added {tick.upper()} to port')
def load(): #load port from json file
    fname = 'test_port.json'
    if os.path.exists(fname):
        try:
            with open(fname, 'r') as f:
                port = json.load(f)
            for tick in port:
                port[tick] = float(port[tick])
            return port
        except (json.JSONDecodeError, ValueError):
            print('Error')
            return {}
    else:
        return {}
def save(port): #save port to json file
    fname = 'new_port.json'
    try:
        with open(fname, 'w+') as file:
            json.dump(port, file)
    except Exception as e:
        print(f'Error {e}')
def price(tick): # get price from coingecko using the ticker symbol that the user inputs
    coin = COIN_IDS.get(tick.lower())
    if not coin:
        print(f"Ticker '{tick}' not found")
        return None

    url = f'https://api.coingecko.com/api/v3/simple/price?ids={coin}&vs_currencies=usd'

    try:
        link = requests.get(url)
        link.raise_for_status()
        x = link.json()
        y = x[coin]['usd']
        return float(y)
    except requests.RequestException:
        print('Error')
        return None
    except (KeyError, ValueError):
        print('Error')
        return None


def port_value(port, price_call = price): # take port get prices calc value
    tot = 0
    assval = {}
    for tick, quant in port.items():
        y = price_call(tick)
        if y is None:
            assval[tick] = None
            continue
        val = quant * y
        assval[tick] = val
        tot = tot + val
    return tot, assval



def display_port(port):
    if not port:
        print('Empty port, inflation is your enemy')
        return
    tot, assval = port_value(port)
    print('Port Overview: ')
    for tick, val in assval.items():
        quant = port[tick]
        if val is None:
            print(f'{tick.upper()} price not available')
        else:
            y = val / quant
            print(f'{tick.upper()}: {quant} at ${y:.2f} = ${val:.2f}')
    print(f'Your port is worth: ${tot:.2f}')
def clean_quant():
    while True:
        user_input = input('Enter Quantity: ').strip()
        try:
            quant = float(user_input)
            if quant <= 0:
                print('The quantity of the coin must be larger than zero')
            else:
                return quant
        except ValueError:
            print('Enter a larger number of the currency to add')



if __name__ == '__main__':
    main()
