# Python Çukur Tespit

Projenin amacı, bir video kaynağındaki çukurları tespit etmek ve bunların koordinatlarını kaydetmek. Kod, YOLOv4 Tiny modelini kullanarak çukur tespiti yapıyor ve tespit edilen çukurların koordinatlarını bir metin dosyasında saklıyor. Ayrıca, çukurların tespit edildiği karelerin görüntüleri de kaydediliyor.

Kodun çalışma mantığı aşağıdaki adımlardan oluşuyor:

#1 Nesne sınıflarının adlarının "obj.names" dosyasından okunması.
#2 YOLOv4 Tiny modelinin tanıtılması ve parametrelerinin girilmesi.
#3 Video kaynağının tanıtılması ve sonuç kaydı için VideoWriter nesnesinin tanıtılması.
#4 Tespit yapılacak döngünün başlatılması.
#5 Her bir karede çukur tespiti yapılması ve tespit edilen çukurların koordinatlarının metin dosyasına kaydedilmesi.
#6 Tespit edilen çukurların karelerinin görüntülerinin kaydedilmesi.
#7 FPS değerinin hesaplanması ve ekrana yazdırılması.
#8 Sonuçların ekrana ve video kaydına yazdırılması.

Kod, "project_files" klasöründe "yolov4_tiny.weights" ve "yolov4_tiny.cfg" dosyalarını kullanıyor. Ayrıca, "geocoder" kütüphanesi de kullanılıyor. Tespit edilen çukurların koordinatları "pothole_coordinates" klasöründe saklanıyor ve görüntüler "pothole_coordinates" klasörüne kaydediliyor.


# Çukur Tespiti Projesi
Bu proje, bir video kaynağındaki çukurları tespit etmek ve bunların koordinatlarını kaydetmek için bir görüntü işleme uygulamasıdır. YOLOv4 Tiny modeli kullanılarak çukur tespiti yapılmakta ve tespit edilen çukurların koordinatları bir metin dosyasında saklanmaktadır.

# Kullanılan Kütüphaneler
cv2
geocoder
time
os

# Kullanılan Dosyalar
yolov4_tiny.weights
yolov4_tiny.cfg
obj.names

# Nasıl Kullanılır?
Yukarıdaki kütüphaneleri ve dosyaları indirin ve projenin bulunduğu klasöre yerleştirin.
Video kaynağını "test-karsiyaka.mp4" olarak değiştirin veya kendi videonuzu kullanın.
Proje dosyasını çalıştırın.
Çukurların tespit edildiği karelerin görüntüleri "pothole_coordinates" klasöründe kaydedilecektir. Ayrıca, her çukurun koordinatları "coordinates.txt" dosyasına da yazdırılacaktır. Bu dosyada, her çukurun koordinatları ayrı bir satırda listelenir.

<h1>deneme<h1>
