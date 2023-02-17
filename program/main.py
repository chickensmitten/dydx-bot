
from func_connections import connect_dydx

if __name__ == "__main__":
  # connect to client
  try:
    print("Connecting to client... ")
    client = connect_dydx()
  except Exception as e:
    print("Error connecting to client: ", e)
    exit(1)


