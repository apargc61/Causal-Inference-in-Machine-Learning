# import stock_info module from yahoo_fin
#reference 
# !pip install requests-html
import requests
import ssl
ssl._create_default_https_context = ssl._create_unverified_context
import pandas as pd
from yahoo_fin import stock_info as si
from yahoo_fin.stock_info import get_data, tickers_sp500, tickers_nasdaq, tickers_other, get_quote_table
import matplotlib.pyplot as plt
import numpy as np

def sp_100_with_company_name(listonly=False):
    sp100 = pd.read_html("https://en.wikipedia.org/wiki/S%26P_100")[2]
    sp100["Symbol"] = sp100["Symbol"].str.replace(".", "-")
    if listonly:
        sp100_tickers = sp100.Symbol.tolist()
        sp100_tickers = sorted(sp100_tickers)     
        return sp100_tickers
    return sp100

def sp_500():
    sp500 = pd.read_html("https://en.wikipedia.org/wiki/List_of_S%26P_500_companies")[0]
    sp500["Symbol"] = sp500["Symbol"].str.replace(".", "-")
    sp_tickers = sp500.Symbol.tolist()
    sp_tickers = sorted(sp_tickers)
    return sp_tickers

sp100 = sp_100_with_company_name()

def company_info(x):
    selected_company = sp100[sp100['Symbol'] == x]
    return x, selected_company['Name'].values[0], selected_company['Sector'].values[0]

def track_plot():
    tracking = []
    trackingB = []
    for x in sp100.Symbol.tolist():
        vars()[x] = get_data(x)
        # vars()[x] = vars()[x][(vars()[x].index>'2017-01-01')]
        # plt.plot(vars()[x].index, vars()[x]['close'], 'r')
        # plt.title(print(company_info(x),'Stock Price'))
        # plt.ylabel('Price ($)')
        # plt.show()
        vars()[x] = vars()[x][(vars()[x].index>'2023-01-01')]
        increase_table = vars()[x]['close'].rolling(3).apply(lambda x: np.all(np.diff(x) < 0)).astype('boolean')
        increase_table.sum()
        tracking.append({'stock': {company_info(x)}, 'score' : increase_table.sum()})    
        trackingB.append({'stock': x, 'score' : increase_table.sum()})
    return trackingB
           
# have market cap as in the index so that we can see how large is the company as well
# is this the list?? # Get the list of S&P 100 symbols
#sp100_symbols = ['AAPL', 'MSFT', 'GOOGL', 'AMZN', 'FB', 'JPM', 'V', 'PG', 'INTC', 'CSCO', 'C', 'VZ', 'T', 'IBM', 'XOM', 'BA', 'DIS', 'HD', 'GS', 'WMT', 'MCD', 'NKE', 'KO', 'PEP', 'JNJ', 'CVX', 'MRK', 'PFE', 'SPG', 'ABBV', 'TXN', 'TSLA', 'NFLX', 'COST', 'UNH', 'PYPL', 'GOOG', 'ORCL', 'AVGO', 'ACN', 'AMGN', 'INTU', 'GS', 'MS', 'GE', 'LMT', 'MMM', 'MSI', 'SO', 'ABT', 'MDT', 'DHR', 'LIN', 'UPS', 'LOW', 'BLK', 'AXP', 'CAT', 'RTX', 'USB', 'CVS', 'TMO', 'ADBE', 'CME', 'ADP', 'PM', 'ISRG', 'FIS', 'FDX', 'TMUS', 'LRCX', 'AMD', 'BDX', 'APD', 'ANTM', 'NOW', 'SCHW', 'ZTS', 'AMD', 'EQIX', 'BIIB', 'FDX', 'MU', 'ICE', 'NSC', 'ITW', 'CHTR', 'CCI', 'ECL', 'EADSY', 'GD', 'KMB', 'EMR', 'ALL', 'PLD']

# pd.DataFrame(tracking).sort_values(by=['score'], ascending=False).head(40)
# # plot the above to se how those graph looks like
# pd.DataFrame(tracking).sort_values(by=['score'], ascending=False).head(30)    

# the biggest drops and dips are seen here 
def sort_and_plot():
    trackingB = track_plot()
    sorted_list = sorted(trackingB, key=lambda x: x['score'], reverse=True)
    sorted_names = [item['stock'] for item in sorted_list]#[0:20]
    for x in sorted_names:
        vars()[x] = get_data(x)
        vars()[x] = vars()[x][(vars()[x].index>'2017-01-01')]
        plt.plot(vars()[x].index, vars()[x]['close'], 'r')
        plt.title(print(company_info(x),'Stock Price'))
        plt.ylabel('Price ($)')
        plt.show()     
sort_and_plot()