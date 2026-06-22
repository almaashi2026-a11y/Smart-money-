import requests
from config import TOKEN, CHAT_ID
from scanner import calculate_rvol
from finvizfinance.screener.overview import Overview

def send_telegram(msg):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    requests.post(url, data={'chat_id': CHAT_ID, 'text': msg})

# فلترة الأسهم - نستخدم طريقة مبسطة لتجنب الأخطاء
foverview = Overview()
foverview.set_filter(price='Under $10') 
stocks = foverview.screener_view()['Ticker'].tolist()

# فحص أول 5 أسهم لتجنب الضغط على الخادم
for ticker in stocks[:5]: 
    rvol = calculate_rvol(ticker)
    if rvol > 2.0:
        send_telegram(f"🚀 تنبيه سيولة: {ticker} | RVOL الحالي: {rvol:.2f}")
        
