import yfinance as yf

aapl = yf.Ticker('AAPL')

print(aapl)

aapl_info = aapl.info

print('AAPL sector: ', aapl_info['sector'])
print('AAPL EBITA Margins: ', aapl_info['ebitdaMargins'])
print('AAPL Profit Margins: ', aapl_info['profitMargins'])
print('AAPL Gross Margins: ', aapl_info['grossMargins'])
print('AAPL Day High: ', aapl_info['dayHigh'])