import yfinance as yf
import pandas as pd

# دالة حساب الـ RVOL الاحترافية
def calculate_rvol(ticker, window=20):
    df = yf.download(ticker, period="1mo", interval="15m")
    df['Vol_SMA'] = df['Volume'].rolling(window=window).mean()
    df['RVOL'] = df['Volume'] / df['Vol_SMA']
    return df

# مثال بسيط للفلترة
def scan_stock(ticker):
    df = calculate_rvol(ticker)
    last_rvol = df['RVOL'].iloc[-1]
    last_price = df['Close'].iloc[-1]
    
    # شرط السعر (بيني) وشرط السيولة (أكثر من 2.5 ضعف)
    if 0.20 <= last_price <= 10.00 and last_rvol > 2.5:
        return True
    return False
  
