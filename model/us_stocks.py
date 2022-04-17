import yfinance as yf

stock_symbol = "MSFT"

stock = yf.Ticker(stock_symbol)
hist = stock.history(period="max")
