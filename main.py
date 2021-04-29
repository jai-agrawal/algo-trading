from utils import *

# Initialsing variables: stock symbol, start and end dates for NSEpy and number of stocks to buy/sell
symbol = 'BHARTIARTL'
start = datetime(2019,1,1)
end = datetime(2021,1,1)
stocks = 100

# Pulling stock data using NSEpy
df = gh(symbol=symbol, start=start, end=end)

# Defining the short, middle and long exponential moving averages for 5,18, and 62 days respectively
df['Short'] = df.Close.ewm(span=5, adjust=False).mean()
df['Middle'] = df.Close.ewm(span=18, adjust=False).mean()
df['Long'] = df.Close.ewm(span=62, adjust=False).mean()

# Inserting Buys and Sells at certain price and date points
df['Buy'], df['Sell'] = buy_sell_function(df)
# Inserting profits using buys and sells as well as number of stocks defined
df['Profits'] = profits(df['Buy'], df['Sell'], stocks)

# save dataframe to CSV
df.to_csv(f'{symbol}.csv', index=False)
