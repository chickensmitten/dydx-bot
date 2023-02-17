from constants import ABORT_ALL_POSITIONS, FIND_COINTEGRATED
from func_connections import connect_dydx
from func_private import abort_all_positions
from func_public import construct_market_prices
from func_cointegration import store_cointegration_results

if __name__ == "__main__":
  # connect to client
  try:
    print("Connecting to client... ")
    client = connect_dydx()
  except Exception as e:
    print("Error connecting to client: ", e)
    exit(1)

if ABORT_ALL_POSITIONS:
  try:
    print("Closing all positions... ")
    close_orders = abort_all_positions(client)
  except Exception as e:
    print("Error closing all positions: ", e)
    exit(1)    

if FIND_COINTEGRATED:
  try:
    print("Fetching market prices, please allow 3 mins... ")
    df_market_prices = construct_market_prices(client)
  except Exception as e:
    print("Error constructing market prices: ", e)
    exit(1)

  try:
    print("Storing cointegrated pairs... ")
    stores_result = store_cointegration_results(df_market_prices)
    if stores_result != "saved":
      print("Error saving cointegrated pairs")
      exit(1)
  except Exception as e:
    print("Error constructing market prices: ", e)
    exit(1)