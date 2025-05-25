import yfinance as yf
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os
os.chdir(os.path.dirname(__file__))

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

# En fazla kazanç sağlayan şirketi bul
if not returns_df.empty:
    returns_df['Percent Change'] = returns_df['Percent Change'].apply(
    lambda x: float(x.iloc[0]) if isinstance(x, pd.Series) else float(x)
)
    best_investment = returns_df['Percent Change'].idxmax()
    best_return = returns_df.loc[best_investment, 'Percent Change']
    print(f"En fazla kazanç sağlayan şirket: {best_investment} (%{best_return:.2f})")
else:
    print("Hisse verisi bulunamadı veya boş DataFrame.")

# 1 aylık hareketli ortalama grafiği
plt.figure(figsize=(18, 10))

for ticker in tickers:
    moving_avg = data[ticker].rolling(window=21).mean()
    plt.plot(moving_avg, label=f'{ticker} 1 Aylık MA')

plt.title('2024 1 Aylık Hareketli Ortalamalar')
plt.xlabel('Tarih')
plt.ylabel('Fiyat ($)')
plt.legend(fontsize=14)
plt.grid(True)

# Pencereyi tam ekran yap
manager = plt.get_current_fig_manager()
try:
    manager.window.showMaximized()
except AttributeError:
    try:
        manager.full_screen_toggle()
    except:
        pass

plt.show()

# DataFrame'e bütün kapanış fiyatlarını birleştirelim
combined_data = pd.concat(data, axis=1)
combined_data.columns = tickers

# Korelasyon matrisi
corr_matrix = combined_data.corr()
print(corr_matrix)

# Değerlendirme fonksiyonu
def degerlendirme(corr_matrix):
    print("\nDeğerlendirme Sonuçları:\n")
    print("Korelasyon matrisindeki köşegen değerler her şirketin kendisiyle olan ilişkisinin 1 olduğunu gösterir.\n")
    print("Aşağıda, şirketler arasındaki kapanış fiyatları korelasyonları ve bu korelasyonların anlamları detaylı olarak açıklanmıştır:\n")
    
    tickers = corr_matrix.columns
    n = len(tickers)
    
    for i in range(n):
        for j in range(i+1, n):
            corr_value = corr_matrix.iloc[i, j]
            company_1 = tickers[i]
            company_2 = tickers[j]
            
            if corr_value >= 0.9:
                yorum = (f"{company_1} ile {company_2} arasında %{corr_value*100:.1f} seviyesinde çok güçlü ve pozitif bir ilişki "
                         "bulunmaktadır. Bu, her iki şirketin hisse fiyatlarının genellikle aynı yönde ve benzer oranda hareket ettiğini gösterir.")
            elif corr_value >= 0.75:
                yorum = (f"{company_1} ve {company_2} hisse fiyatları arasında yüksek düzeyde pozitif korelasyon (%{corr_value*100:.1f}) "
                         "vardır, bu da piyasa koşullarına benzer tepki verdiklerini işaret eder.")
            elif corr_value >= 0.5:
                yorum = (f"{company_1} ile {company_2} arasında orta seviyede pozitif korelasyon (%{corr_value*100:.1f}) vardır. "
                         "Fiyat hareketlerinde zaman zaman paralellik gözlemlenmektedir.")
            elif corr_value >= 0.3:
                yorum = (f"{company_1} ve {company_2} hisse fiyatları arasında zayıf pozitif korelasyon (%{corr_value*100:.1f}) söz konusudur. "
                         "Fiyatlar bazen benzer hareketler gösterse de bu ilişki zayıftır.")
            elif corr_value > -0.3:
                yorum = (f"{company_1} ile {company_2} arasındaki korelasyon (%{corr_value*100:.1f}) nötr veya çok zayıf seviyededir. "
                         "Bu şirketlerin fiyat hareketleri büyük ölçüde birbirinden bağımsızdır.")
            elif corr_value > -0.5:
                yorum = (f"{company_1} ve {company_2} arasında zayıf negatif korelasyon (%{corr_value*100:.1f}) bulunmaktadır. "
                         "Birinin fiyatı artarken diğerinin azalması eğilimi hafifçe görülür.")
            elif corr_value > -0.75:
                yorum = (f"{company_1} ile {company_2} arasında orta seviyede negatif korelasyon (%{corr_value*100:.1f}) vardır. "
                         "Fiyat hareketleri genellikle ters yönde ilerlemektedir.")
            else:
                yorum = (f"{company_1} ve {company_2} arasında çok güçlü negatif korelasyon (%{corr_value*100:.1f}) mevcuttur. "
                         "Biri yükselirken diğeri genellikle düşmektedir, piyasa dinamikleri açısından önemli bir zıtlık söz konusudur.")
            
            print(f"- {yorum}\n")
    
    print("Genel olarak, teknoloji sektöründeki şirketlerin hisse senedi fiyatları arasında çeşitli düzeylerde pozitif ve negatif korelasyonlar gözlemlenmiştir.")
    print("Bu ilişkiler, sektör içi etkileşimler, ortak piyasa koşulları ve yatırımcı davranışları gibi faktörlerden etkilenmektedir.\n")

degerlendirme(corr_matrix)

input("Çıkmak için Enter'a basınız...")