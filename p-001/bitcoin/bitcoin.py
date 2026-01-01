import sys
import requests

if len(sys.argv) < 2:
        sys.exit('Missing command-line argument')
try:
    m = float(sys.argv[1])
except ValueError:
    sys.exit('Command-line argument is not a number')

try:
    r = requests.get('https://rest.coincap.io/v3/assets/bitcoin?apiKey=168150d3d67af36095539f7f009895782baabcdf86d91c97c930d43399e4161c')
    data = r.json()
    btc = float(data['data']['priceUsd'])
    total = btc * m
    print(f"${total:,.4f}")

except requests.RequestException:
    sys.exit

