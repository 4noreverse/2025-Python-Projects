# Crypto Portfolio Python Program aka Port Analyzer 3000
## Video URL: https://youtu.be/OLJTtc-RF6A

## Overview
Python program that a user can add or display their cryptocurrency portfolio, the program supports 10+ coins using data from CoinGecko. The program takes user input as well as a json file that has the users crypto holdings in it with the key being the ticker and the value being the number amount of the coins held.

## Features
Choose between three options, display portfolio, add to portfolio, or quit. Then produces a new json file with the action acted upon. Uses CoinGecko API for live pricing of crypto assets then calculates and displays portfolio and asset value.

## Technologies
JSON for file input and output storing the data of the crypto portfolios. CoinGecko API for the live price of each supported crypto asset.

## About Program
main() - user interaction and menu, option one is used to display portfolio and calls upon the display_port() function. Option two calls upon the crypto function which adds a supported currency to the portfolio.

load() - loads the users JSON portfolio into the program.

save() - saves the data of the portfolio into a new JSON file.

crypto() - adds a supported cryptocurrency to the portfolio when a user selects option two in the menu and takes the quantity of how many of the certain coin the user would like to purchase.

price() - this function gathers the pricing for each asset in portfolio from the dictionary of the supported cryptocurrency from the CoinGecko API.

port_value() - does calculations for the assets and then total portfolio.

clean_quant() - makes sure that the quantity entered when using the menu option number two to add crypto accepts a valid input aka input validation.

display_port() - displays the portfolio and asset value when the user selects option one.

## Modules
requests - used to make HTTP requests allowing the program to talk to the CoinGecko API to gather the live price data for cryptocurrency assets. This also needed 'pip install requests' to be run in the terminal before importing.

json - used to read JSON files into dictionaries, this is used to load the portfolio and then save the data to a JSON file when the program exits.

os - used for file checking and error handling if a file was not found or existed.

## Mock Crypto Portfolio JSON File
{
    "btc":1.5,
    "sol":10,
    "fort":100.5,
    "usdt":50000.25
}
This file is titled test_port.json in the same project folder.


## Example Usage
Choose an option:
1 - view port
2 - add to port
3 - quit

The portfolio used above will produce this output if option 1 is inputted:

Port Overview:
BTC: 1.5 at $87400.00 = $131100.00
SOL: 10.0 at $122.09 = $1220.90
FORT: 100.5 at $0.02 = $2.02
USDT: 50000.25 at $1.00 = $49966.40
Your port is worth: $182289.32

In a new JSON file this:
{"btc": 1.5, "sol": 10.0, "fort": 100.5, "usdt": 50000.25}
will also be created in the output called new_port.json.

## Files
new_port.json is the new file that is created and outputted after the program is run, it contains this: {"btc": 1.5, "sol": 10.0, "fort": 100.5, "usdt": 50000.25} representing a dictionary of the portfolios holdings that was used in the program.

project.py is the python program itself and contains the eight functions and imported modules to complete the processing explained in the overview.

README.md this file gives guidance and descriptions about the written code and program.

requirements.txt shows the installed module requests to be used in the project.py.

test_port.json is the file that contains the mock crypto portfolio used in my demonstration of the program.

test_project.py is the program that tests the created functions in project.py.


