##Dokümantasyon
###Kurulum

Çalıştırmadan önce:

1. `sudo pip install flask` komutuyla Flask bağımlılığını kurun. 

2. `python init_db.py` komutuyla gerekli Sqlite veritabanını oluşturun.

3.  `server.py` dosyası, 15. satırdaki kullanıcı ve şifre bölümünü değiştirin.

4. Yine `server.py` dosyası, 66. satırdaki dinlenecek portu isteğe göre (80 dışında bir port kullanın) seçin ve `debug=False` şeklinde ayarlayın.

 
###Çalıştırma

Bu program bir Webserver oluşturur ve 66. satırda verdiğiniz portu dinler.
