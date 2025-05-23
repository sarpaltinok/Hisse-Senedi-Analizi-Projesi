import yfinance as yf
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Hisse kodları
tickers = ["GOOGL", "MSFT", "META", "AAPL", "AMZN"]

# Verileri indirme
data = {}
for ticker in tickers:
    data[ticker] = yf.download(ticker, start="2024-01-01", end="2025-01-01")['Close']

# Ortalama kapanış fiyatlarını hesapla          
average_close = {}
for ticker in tickers:
    average_close[ticker] = data[ticker].mean()

# Ortalama kapanış fiyatlarını DataFrame'e dönüştür
average_close_df = pd.DataFrame(list(average_close.items()), columns=['Company', 'Average_Close'])

# DataFrame'i göster
print(average_close_df)

# 2024 yılında en yüksek kapanış fiyatına ulaşan şirket ve tarihi bul
max_close_info = {}  
for ticker in tickers:
    max_price = data[ticker].max()
    max_date = data[ticker].idxmax()
    max_close_info[ticker] = {'Max Price': max_price, 'Date': max_date}

# Göster
max_close_df = pd.DataFrame(max_close_info).T
print(max_close_df)

# Yüzde değişim hesapla
returns = {}
for ticker in tickers:
    first_price = data[ticker].iloc[0]
    last_price = data[ticker].iloc[-1]
    pct_change = ((last_price - first_price) / first_price) * 100
    returns[ticker] = {
        'First Price': first_price,
        'Last Price': last_price,
        'Percent Change': pct_change}
    
returns_df = pd.DataFrame(returns).T
print(returns_df)  

# En fazla kazanç sağlayan şirket
best_investment = returns_df['Percent Change'].idxmax()
print(f"En fazla kazanç sağlayan şirket: {best_investment}")

# 1 aylık hareketli ortalama grafiği
plt.figure(figsize=(14, 7))  

for ticker in tickers:
    # Kapanış fiyatları üzerinden 1 aylık hareketli ortalama hesapla
    moving_avg = data[ticker].rolling(window=21).mean()
    plt.plot(moving_avg, label=f'{ticker} 1 Aylık MA')  

# Grafik başlıkları ve etiketler
plt.title('2024 1 Aylık Hareketli Ortalamalar')
plt.xlabel('Tarih')
plt.ylabel('Fiyat ($)')
plt.legend()  
plt.grid(True)  
plt.show()

# Korelasyon matrisi
# DataFrame'e bütün kapanış fiyatlarını birleştirelim
combined_data = pd.concat(data, axis=1)
combined_data.columns = tickers  # Sütun isimlerini hisse kodlarıyla güncelle

# Korelasyon matrisi
corr_matrix = combined_data.corr()
print(corr_matrix)

# YORUM
print("\nYORUM:")
print("-Diagonal (köşegen) değerler: Her şirketin kendisiyle olan korelasyonu doğal olarak 1'dir.")
print("-GOOGL ve MSFT (0.743): Google ve Microsoft'un kapanış fiyatları arasında güçlü bir pozitif ilişki vardır.")
print("-META ve AMZN (0.825): Meta ve Amazon'un fiyatları arasında oldukça güçlü bir pozitif ilişki gözlemleniyor.")
print("-AAPL ve MSFT (0.545): Apple ve Microsoft'un fiyatları arasında daha zayıf bir pozitif ilişki var.")
print("\nGenel olarak, teknoloji şirketlerinin hisse fiyatlarının birbirine oldukça bağlı olduğu söylenebilir.")