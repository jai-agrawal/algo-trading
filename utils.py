import pandas as pd
import numpy as np
from math import isnan
from nsepy import get_history as gh
from datetime import datetime

# function to evaluate when to buy and sell
def buy_sell_function(data):
    buy_list = []
    sell_list = []
    flag_long = False
    flag_short = False
    for i in range(0,len(data)):
        # main algorithm which allows for stocks to be bought and sold
        if data['Middle'][i] < data['Long'][i] and data['Short'][i] < data['Middle'][i] and flag_long == False and flag_short == False:
            buy_list.append(data['Close'][i])
            sell_list.append(np.nan)
            flag_short = True
            prev_buy_value = data['Close'][i]
        elif flag_short == True and data['Short'][i] > data['Middle'][i] and prev_buy_value < data['Close'][i]:
            buy_list.append(np.nan)
            sell_list.append(data['Close'][i])
            flag_short = False
        elif data['Middle'][i] > data['Long'][i] and data['Short'][i] > data['Middle'][i] and flag_long == False and flag_short == False:
            buy_list.append(data['Close'][i])
            sell_list.append(np.nan)
            flag_long = True
            prev_buy_value = data['Close'][i]
        elif flag_long == True and data['Short'][i] < data['Middle'][i] and prev_buy_value < data['Close'][i]:
            buy_list.append(np.nan)
            sell_list.append(data['Close'][i])
            flag_long = False
        else:
            buy_list.append(np.nan)
            sell_list.append(np.nan)
    # exception for last date of the data in which all remaining assets are sold
    if len([x for x in sell_list if isnan(x) == False]) < len([x for x in buy_list if isnan(x) == False]):
        sell_list[-1] = float(data['Close'].tail(1))
    return buy_list, sell_list

# function to find profits using buy and sell lists
def profits(buys, sells, stocks):
    profits = []
    for i in range(len(buys)):
        if isnan(buys[i]) == False:
            profits.append(-buys[i] * stocks)
        elif isnan(sells[i]) == False:
            profits.append(sells[i] * stocks)
        else:
            profits.append(0)
    return profits

# function to pass in dataframe and return transformed dataset with EMAs and profits
def dataset(df, stocks):
    df['Short'] = df.Close.ewm(span=5, adjust=False).mean()
    df['Middle'] = df.Close.ewm(span=18, adjust=False).mean()
    df['Long'] = df.Close.ewm(span=62, adjust=False).mean()
    df['Buy'], df['Sell'] = buy_sell_function(df)
    df['Profits'] = profits(df['Buy'], df['Sell'], stocks)
    return df

# function to find profits and return dataframe
def find_profits(symbol, start, end, stocks= 50):
    df = gh(symbol=symbol, start=start, end=end)
    df = dataset(df, stocks)
    print(f"Profit: {df['Profits'].sum()}")
    return df


