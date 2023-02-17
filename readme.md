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

## Operation
Constants
- Amount
- Mode
- Trigger
- Key Imports


- Get Prices
- Manage Open Trades
- Cler All Trades
- Open Trades
