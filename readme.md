# DYDX Bot

## Setup Instructions
- Have Metamask wallet, change to Goerli Network
- Go to Goerli Faucet to send ETH
- Head to DYDX exchange to connect wallet with Goerli test network, remember to click on "remember me"
- Then inspect element -> Application -> Local Storage -> "trade.stage.dydx.exchange" -> find "STARK_KEY_PAIRS" and "API_KEY_PAIRS"
- Information to collect for DYDX to add to `.env`:
  - ETHEREUM ADDRESS
  - ETH PRIVATE KEY
  - STARK PRIVATE KEY
  - DYDX API KEY
  - DYDX API SECRET
  - DYDX API PASSPHRASE
  - HOST = API_HOST_GOERLI
- check python version with `python3 --version`
- create a python virtual environment with `python3 -m venv venv`
- run `source venv/bin/activate`
- run `pip3 install -r requirements.txt`. requirements.txt is found in the course resources
- then initialize git, `git init`
- in `.gitignore` add `.env` and `venv` to ignore these files and folders

## Start
- in root, run `source venv/bin/activate` to activate venv environment
- go to `cd program`
- run `python3 main.py`
- there should be output below:
```
Connection Successful
Account ID:  <ID>
Quote Balance:  <Amount>
```
- run `deactive` to exit venv environment

## Operation
- Connect to DYDX
- Place Market Order
- Abort All Open Orders
- Construct Market Prices & Store Cointegrated Pairs: Find all market prices pairs, put them in table and find, based on the prices, which one is cointegrated.
  - Get ISO times: refer to DYDX `fromISO` and `toISO`, with `limit`
  - Get historical candles
  - Construct market prices
  - Write conintegration functions
  - Find and store cointegration pairs
- While True
  - Manage Existing Trades & Open Positions
    - Create bot agent class
      - Open Trades
      - Check Validity of Order Status by ID
    - Get recent candles
    - Check if exit and exit open trades
    - Check open positions
    - Place and save trades

## Deploying to AWS EC2
- Upload code and venv, add environment variable and add cron job.
- Create security groups with preferred name with description on the permissions like `Allows SSH for developers`
  - Add rule of SSH type and allow all IP addresses. Then create security group.
- Go to EC2, launch instances, Amazon aws and ubuntu are normally free tier. Select ubuntu
- For architecture, might want to select ARM if using ARM, else, select Intel x86
- Create key pair is recommended
- Click on "Actions", click on "Connect" and "Connect"
- Go into ubuntu terminal
  - `sudo apt-get update`
  - `python --version` then install `sudo apt-get install python3.10`
  - `pip3 freeze > requirements.txt` to update the file


## Explanation on Files
- `__pycache__` is a folder for compiled python 3 bytecode
- `constants.py` contains all the constants. It also functions as on-off switch for specific functions
- `func_connections.py` contains connection to DYDX. 
- `func_private.py` contains execution functions that requires private keys
- `func_public.py` contains execution functions that are public
- `func_utils.py` contains commonly shared functions
- `func_cointegration.py` contains code to caculate and store cointegration. `calculate_zscore`, `calculate_half_life`, `calculate_cointegration` contains battle tested code, suitable for production.
- `func_bot_agent.py` builds bot agents. In `open_trades`, two orders will be opened because for the cointegration to work, you need two opposing trades to converge.
- `func_open_positions.py` will open trading positions
- `func_messaging.py` will send messages to telegram

## Miscellaneous
- `f-string` is a new string formatting mechanism known as Literal String Interpolation or more commonly as F-strings (because of the leading f character preceding the string literal). The idea behind f-strings is to make string interpolation simpler. 
```
val = 'Geeks'
print(f"{val}for{val} is a portal for {val}.")
 
name = 'Tushar'
age = 23
print(f"Hello, My name is {name} and I'm {age} years old.")
```
- use `breakpoint()` to debug
- testnet data is not as accurate as mainnet data. To do backtesting, use mainnet data without real trading.

## KIV
- Order expiration less than 1 minute
Got the following error `Error closing all positions:  DydxApiError(status_code=400, response={'errors': [{'msg': 'Order expiration cannot be less than 1 minute(s) in the future'}]})`. It is likely related to this code. `expiration = datetime.fromisoformat(server_time.data["iso"].replace("Z", "")) + timedelta(seconds=70)` It is likely a GMT error, have to added more `seconds`
