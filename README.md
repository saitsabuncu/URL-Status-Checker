```markdown
# URL Status Checker

**URL Status Checker**, verilen bir dizi URL'nin erişilebilir olup olmadığını kontrol eder, HTTP durum kodlarını raporlar ve yanıt sürelerini analiz eder. Bu araç, web geliştiricileri ve sistem yöneticileri için web adreslerinin durumunu hızlıca kontrol etmek için tasarlanmıştır.

---

## 🚀 Özellikler

- **Erişilebilirlik Kontrolü**: Belirtilen URL'lerin erişilebilir olup olmadığını kontrol eder.
- **HTTP Durum Kodu**: Her URL'nin HTTP durum kodunu ve durum mesajını (OK, Not Found vb.) döndürür.
- **Yanıt Süresi**: Her bir URL için sunucunun yanıt süresini ölçer.
- **Hata Yönetimi**: Erişilemeyen URL'ler için ayrıntılı hata mesajları verir.

---

## 📂 Proje Yapısı

```plaintext
project/
├── main.py             # Projenin ana Python dosyası
├── urls.txt            # Kontrol edilecek URL listesini içeren dosya (isteğe bağlı)
├── README.md           # Proje açıklamaları
```

---

## 🔧 Kurulum

### 1. Gerekli Kütüphaneleri Yükleyin
Proje için aşağıdaki Python kütüphaneleri gereklidir:
```bash
pip install requests
```

### 2. Projeyi Çalıştırın
Proje dizininde terminal veya bir IDE kullanarak şu komutu çalıştırın:
```bash
python main.py
```

---

## 📜 Kullanım

### Örnek URL Listesi
Python kodunda veya bir `urls.txt` dosyasında kontrol edilecek URL'leri belirtin. Örneğin:
```plaintext
https://www.google.com
https://www.github.com
https://nonexistent.example
```

### Çalıştırma
1. **Kullanıcı tarafından belirtilen URL'ler**:
   - Programda önceden tanımlanmış URL'ler üzerinde çalışır.
2. **Ekran Çıktısı**:
   Program her bir URL için durum bilgilerini şu şekilde yazdırır:
   ```
   URL: https://www.google.com | Durum Kodu: 200 | Durum: OK | Yanıt Süresi: 0.15 sn
   URL: https://nonexistent.example | Hata: HTTPSConnectionPool(host='nonexistent.example', port=443): Max retries exceeded with url: /
   ```

---

## 🌟 Geliştirme Önerileri

- **Sonuçları Dosyaya Kaydetme**:
  - Kontrol sonuçlarını bir **CSV** veya **JSON** dosyasına kaydederek analiz edilebilir hale getirin.
  
- **Asenkron İstekler**:
  - **asyncio** ve **aiohttp** kullanarak isteklerin daha hızlı yapılmasını sağlayın.

- **Kullanıcı Girdisi**:
  - Kullanıcıdan interaktif olarak URL listesi almak için bir menü sistemi ekleyin.

- **GUI (Grafik Arayüz)**:
  - **Tkinter** veya **PyQt** ile bir masaüstü uygulaması geliştirin ve sonuçları görselleştirin.

---

## 🛠️ Lisans

Bu proje MIT Lisansı ile lisanslanmıştır. Daha fazla bilgi için `LICENSE` dosyasını inceleyin.

---

## ✨ İletişim

Herhangi bir soru veya öneriniz varsa, lütfen [sabuncumustafasait@gmail.com](mailto:your_email@example.com) adresinden iletişime geçin.
```
