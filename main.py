import requests
from config import TOKEN, CHAT_ID
from scanner import calculate_rvol
from finvizfinance.screener.overview import Overview

def send_telegram(msg):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    requests.post(url, data={'chat_id': CHAT_ID, 'text': msg})

# فلترة الأسهم البيني
foverview = Overview()
foverview.set_filter(price_lt='10', volume_gt='500k')
stocks = foverview.screener_view()['Ticker'].tolist()

for ticker in stocks[:10]: # فحص أول 10 أسهم كمثال
    rvol = calculate_rvol(ticker)
    if rvol > 2.5:
        send_telegram(f"فرصة قوية: {ticker} | RVOL: {rvol:.2f}")
      
