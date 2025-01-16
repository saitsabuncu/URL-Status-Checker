import requests
from time import time

# URL listesi
urls = [
    "https://www.google.com",
    "https://www.github.com",
    "https://www.nonexistentwebsite.example",
    "https://www.python.org"
]


def check_url_status(url_list):
    """
    URL'lerin durumlarını kontrol eder ve raporlar.

    Args:
        url_list (list): Kontrol edilecek URL'lerin listesi.

    Returns:
        list: Her URL'nin durumu ve HTTP bilgilerini içeren sonuçlar.
    """
    results = []
    for url in url_list:
        try:
            start_time = time()
            response = requests.get(url, timeout=5)
            end_time = time()

            # Başarı durumunda sonuç ekle
            results.append({
                "url": url,
                "status_code": response.status_code,
                "reason": response.reason,
                "response_time": round(end_time - start_time, 2)  # Yanıt süresi
            })
        except requests.exceptions.RequestException as e:
            # Hata durumunda sonucu ekle
            results.append({
                "url": url,
                "error": str(e)
            })
    return results


# URL'leri kontrol et
url_statuses = check_url_status(urls)

# Sonuçları yazdır
for status in url_statuses:
    if "error" in status:
        print(f"URL: {status['url']} | Hata: {status['error']}")
    else:
        print(f"URL: {status['url']} | Durum Kodu: {status['status_code']} | "
              f"Durum: {status['reason']} | Yanıt Süresi: {status['response_time']} sn")
