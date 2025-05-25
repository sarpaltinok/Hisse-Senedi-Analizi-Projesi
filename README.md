[English](https://github.com/brgkdm/Hisse-Senedi-Analizi-Projesi/blob/main/README_EN.md)

# Hisse Senedi Analizi Projesi

Bu proje, belirli teknoloji şirketlerinin hisse senedi verilerini analiz etmek için Python ve çeşitli veri analizi kütüphanelerini kullanır. Proje, hisse senedi fiyatlarının ortalama değerlerini, en yüksek kapanış fiyatlarını, yüzde değişimlerini ve korelasyonlarını hesaplar.

## Kullanılan Kütüphaneler

- **yfinance:** Hisse senedi verilerini çekmek için kullanılır.  
- **pandas:** Veri işleme ve analiz için kullanılır.  
- **numpy:** Sayısal hesaplamalar için kullanılır.  
- **matplotlib:** Veri görselleştirme için kullanılır.  

## Proje Adımları

### 1. Veri Çekme
`yfinance` kütüphanesi kullanılarak Google (GOOGL), Microsoft (MSFT), Meta (META), Apple (AAPL) ve Amazon (AMZN) hisse senetlerinin 2024 yılına ait kapanış fiyatları çekilir.

### 2. Ortalama Kapanış Fiyatları
Her hisse senedi için 2024 yılı boyunca ortalama kapanış fiyatı hesaplanır ve bir tablo halinde gösterilir.

### 3. En Yüksek Kapanış Fiyatı
Her hisse senedi için 2024 yılındaki en yüksek kapanış fiyatı ve bu fiyatın gerçekleştiği tarih bulunur.

### 4. Yüzde Değişim
Her hisse senedi için yılın ilk ve son kapanış fiyatları arasındaki yüzde değişim hesaplanır. En fazla kazanç sağlayan şirket belirlenir.

### 5. Hareketli Ortalama
Her hisse senedi için 1 aylık (30 günlük) hareketli ortalama hesaplanır ve tüm şirketlerin hareketli ortalamaları aynı grafik üzerinde gösterilir.

### 6. Korelasyon Matrisi
Tüm şirketlerin günlük kapanış fiyatları kullanılarak korelasyon matrisi hesaplanır. Fiyat hareketlerinin birbiriyle olan ilişkisi analiz edilir.

## Sonuçlar

- **Ortalama Kapanış Fiyatları:** Her hisse senedinin 2024 yılı boyunca ortalama kapanış fiyatları hesaplanmış ve tablo halinde sunulmuştur.
- **En Yüksek Kapanış Fiyatı:** Her hisse senedi için en yüksek kapanış fiyatı ve bu fiyatın gerçekleştiği tarih belirlenmiştir.
- **Yüzde Değişim:** Hisse senetlerinin yıl boyunca gösterdiği performans yüzde değişim olarak hesaplanmış ve en fazla kazanç sağlayan şirket belirlenmiştir.
- **Hareketli Ortalama:** 1 aylık hareketli ortalamalar grafik üzerinde gösterilerek hisse senetlerinin trendleri karşılaştırılmıştır.
- **Korelasyon Matrisi:** Hisse senetleri arasındaki fiyat hareketlerinin benzerliği korelasyon matrisi ile analiz edilmiş ve yorumlanmıştır.

## Nasıl Çalıştırılır?

 Gerekli kütüphaneleri yükleyin:

```bash
pip install yfinance pandas numpy matplotlib
```

## Türkçe Karakter Sorunu;

- Python projelerinde, özellikle Windows ortamında veya farklı kodlama ayarlarıyla çalışırken, Türkçe karakterler (ç, ğ, ş, ü, ö, İ, ı) konsolda, dosya isimlerinde veya çıktı dosyalarında bozuk veya garip karakterler olarak görünebilir.

- Bu analiz projesinde, eğer "Python Sertifika" dosyası Türkçe karakter içeren bir dosya yolunda bulunuyorsa hata alınması doğaldır.

### Çözüm için şu adımları uygulayabilirsiniz:

1. Python klasörünü bulun:
- Genellikle şu yoldadır:

- "C:\Users\kullanıcı_adınız\AppData\Local\Programs\Python"

2. Python klasörünü Türkçe karakter içermeyen bir konuma taşıyın:
- Örneğin, C:\Python gibi bir klasöre taşıyabilirsiniz.
- (Taşıma işlemi için CTRL+X ve CTRL+V kullanabilirsiniz.)

3. Analiz scriptinizi tekrar çalıştırın:
- Bu işlem sonrası sorun büyük ihtimalle çözülecektir.

## Katkıda Bulunma
Bu proje açık kaynaklıdır. Katkıda bulunmak için fork edip pull request gönderebilirsiniz.

## Proje Ortakları
- [Sarp Altınok](https://github.com/sarpaltinok)
- [Berat](https://github.com/brgkdm)
## Lisans
Bu proje MIT lisansı altında lisanslanmıştır. Daha fazla bilgi için LICENSE dosyasını inceleyin.
