# AccenturePriority

Hepsiburada.com e-ticaret sitesinin otomasyon testleri yazıldı.
Python proglamlama dili ile yazıldı. Versiyon olarak  Python 3.9 kullanıldı.
Design pattern olarak Page Object Model yapısı implemente edildi. 
Test framework'u olarak Pytest kullanıldı. 
Selenium, Pytest, pytest-html, pytest-xdist, Openpyxl, Allure-pytest paketleri projeye yüklendi.
Pytest-html testlerin sonucunda html raporu olusturmak icin kullanıldı. 
Pytest-xdist testleri paralel koşabilmek için implemente edildi.
Openpyxl, Excel dosyalarını okuyabilmek için implemente edildi. 
Common value'lar Configurations altındaki config.ini dosyasından okunmakta. Bu dosya utility altındaki readproperties dosyası tarafından testclass'larına iletilmekte.
Loglama için python'ın 'logging' class'i kullanıldı. Loglar 'Logs' klasorunun altinda automation.log dosyasında tutulmakta. Loglama formatı utilities klasoru altındaki 
customLogger class'inda yazildi.
Success ya da fail case'lerde ekran görüntüsü Screenshots klasörü altında tutuluyor.
Raporlar Reports klasörü altında olusacak sekilde ayarlandı. 
Sonradan projeye implemente edilen pytest-html-reporter ile görsel olarak daha güzel raporlar html olarak olusmaktadir root directory altında. 
Data driven test kosabilmek icin TestData klasoru altında login icin kullanılabilecek datalardan olusan bir excel dosyası implemente edildi. Excel üzerindeki okuma işlemleri de
utilities klasoru altındaki XLUtils class'i üzerindeki methodlarla yapıldı.

Testler terminalden aşağıdaki komutla triggerlanmaktadır. 
Hangi test dosyası calistiralacaksa onun adının kullanılması gerekiyor. Browser kullanımı parametreye bağlanmıştır. chrome yerine edge yazıldığı zaman testler Edge browserda kosacaktır. 
--html ile html raporu belirtilen dosyanın altında olusmaktadir. 
-v parametresi testlerin ayrıntılı cıktısını olusturur. 

pytest -v --html=Reports\report.html testCases\test_login.py --browser chrome
