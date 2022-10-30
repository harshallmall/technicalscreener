import talib
import yfinance as yf

data = yf.download("SPY", start="2020-01-01", end="2020-08-01")

morningstar = talib.CDLMORNINGSTAR(data['Open'], data['High'], data['Low'], data['Close'])

engulfing = talib.CDLENGULFING(data['Open'], data['High'], data['Low'], data['Close'])

data['Morning Star'] = morningstar
data['Engulfing'] = engulfing

engulfing_days = data[data['Engulfing'] != 0]

print(engulfing_days)