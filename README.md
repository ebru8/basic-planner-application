Basic Planner Application 
=========================
Yazılım Yapımı dersi için yapılan takvim ve planlayıcı uygulaması ödevidir.
---------------------------------------------------------------------------

# Kullanıcı tipleri:
1.Admin
2.Users

# Olaylar:
1.işlem Zamanı
2.Olay Başlangıç Zamanı
3.Olay Tanımı
4.Olay Tipi
5.Olay Açıklaması

# Zaman:
Olay Başlangıç Zamanı: ay/gün/yıl , Saat: saat/dakika (GUI'de gösterilmiyor ama saniye ve salise bilgileri mevcut)

# Proje Detayları:
## Projeye dair yazılım özellikleri
Kullanılan IDE : PyCharm Community Edition 2022.3.1
Kullanılan dil: Python 3.9.13
Kullanılan kütüphaneler:
- tkinter: Python diline ait bir arayüz kütüphanesidir ve GUI (Grafiksel Kullanıcı Arayüzü) uygulamaları geliştirmek için kullanılır.
- ttk: tkinter'ın bir alt modülüdür ve daha modern ve gelişmiş görünümlü widget'lar sağlar.
- messagebox: tkinter'ın bir alt modülüdür ve pencere üzerinde iletişim kutuları (mesaj kutuları) oluşturmak için kullanılır.
- datetime: Python'ın standart kütüphanesidir ve tarih ve saat ile ilgili işlemleri yapmak için kullanılır.
- timedelta: datetime kütüphanesinde bulunan bir sınıftır ve tarih ve saat arasındaki farkları temsil etmek için kullanılır.
- playsound: Ses dosyalarını çalmak için kullanılan bir kütüphanedir.
- tkcalendar: tkinter ile uyumlu bir takvim widget'ı sağlar.

## Proje GUI özellikleri:
1. Giriş Yap Ekranı:
  *Kullanıcı adı ve Şifre girilmesi istenip ardından Giriş Yap'a tıklanması gerekmektedir.
  *Eğer Kayıtlı kullanıcı değil ise Kayıt Ol ekranından kayıtlanma beklenmektedir.

2. Kayıt Ol Ekranı:
  *Ad, Soyad, Kullanıcı adı, Şifre, Kimlik numarası, Telefon numarası, Mail adresi, Adres bilgilerinin girilmesi beklenmektedir.
  *Kullanıcı tipi seçilmesi gerekmektedir. Kullanıcı tipleri Standart ve Admin olmak üzere 2 tiptir.
  *Kayıtlı kullanıcı bilgileri users.txt adlı text dosyasına kaydedilip orada tutulmaktadır.

3. Ana Ekran:
  *Olayların sıralandığı bir panel ile Olay Ekle, Olay Düzenle, Olay Sil, Çıkış Yap seçeneklerinden oluşmaktadır.
  *Olay Panelinde eklenen olaylara ait İşlem Zamanı, Olay Başlangıç Zamanı, Olay Tanımı, Olay Tipi, Olay Açıklaması gösterilmektedir.
  *Olay eklemek için Olay Ekle Ekranından bilgilerin girilmesi gerekmektedir.
  *Olayları düzenlemek için Olay Düzenle Ekranından bilgilerin değiştirilmesi gerekmektedir.
  *Olayları silmek için, silinmek istenen olay ekrandan seçilip Olay Sil tuşuna basılmalıdır.
  *Çıkış yapmak için ekrandaki Çıkış Yap tuşuna tıklanmalıdır. Çıkış Yap' tıklanıldıktan sonra program kapanmaktadır.

4. Olay Ekle:
  *İsteğe bağlı olarak Alarm Ayarla seçeneğinden olay zamanında hatırlatıcı olması için alarm eklenebilmektedir. Alarmın çalınması için zaman bilgileri Erken Alarm kısmına saniye cinsinden girilmelidir.
  *Olay Başlangıç zamanı ekrandaki takvimden seçilmelidir veya manuel olarak yazılmalıdır. Zaman Bilgileri ay/gün/yıl olarak girilmelidir.
  *Olay Saati saat:dakika olarak girilmelidir.
  *Olay Tanımı, Olay Tipi ve Olay Açıklaması isteğe bağlı olarak girilmelidir.

- Olay Düzenle:
  *Düzenlenilmek istenen olay Ana Ekrandan seçildikten sonra Olay Düzenle ekranı gelmektedir.
  *Ekranda Kullanıcı adı, Veri 1 olarak İşlem zamanı, Veri 2 olarak Olay Başlangıç zamanı, Veri 3 olarak Olay tanımı, Veri 4 olarak Olay tipi ve Veri 5 olarak Olay açıklaması bulunmaktadır.
  *Değiştirilmek istenen veri düzeltildikten sonra Kaydet tuşu ile kaydedilmektedir.




