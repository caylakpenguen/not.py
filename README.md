##Dokümantasyon
###Kurulum

Çalıştırmadan önce:

0. `sudo apt-get install python-pip` komutuyla pip kurun.

1. `sudo pip install flask` komutuyla Flask bağımlılığını kurun. 

2. `python init_db.py` komutuyla gerekli Sqlite veritabanını oluşturun.

3.  `server.py` dosyası, 15. satırdaki kullanıcı ve şifre bölümünü değiştirin.

4. Yine `server.py` dosyası, 66. satırdaki dinlenecek portu isteğe göre (80 dışında bir port kullanın) seçin ve `debug=False` şeklinde ayarlayın.

 
###Çalıştırma

screen -A -m -d -S notpyserver python server.py

Bu program bir Webserver oluşturur ve 66. satırda verdiğiniz portu dinler.

#### Nginx ve Apache Yapılandırması için.

### Nginx icin site yapılandırma dosyasına ekleyin.

`location /not {
proxy_pass http://127.0.0.1:8080/not;
}`

`service nginx restart`

### Apache

Önce Modülü aktif edin
`a2enmod proxy_http`

Yapılandırma Dosyanıza Ekleyin
`ProxyPass /not http://127.0.0.1:8080/not`

Son olarak
`service apache2 restart`

