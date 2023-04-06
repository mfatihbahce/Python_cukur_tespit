# Python Çukur Tespit

Projenin amacı, bir video kaynağındaki çukurları tespit etmek ve bunların koordinatlarını kaydetmek. Kod, YOLOv4 Tiny modelini kullanarak çukur tespiti yapıyor ve tespit edilen çukurların koordinatlarını bir metin dosyasında saklıyor. Ayrıca, çukurların tespit edildiği karelerin görüntüleri de kaydediliyor.

Kodun çalışma mantığı aşağıdaki adımlardan oluşuyor:

<h5>#1 Nesne sınıflarının adlarının "obj.names" dosyasından okunması.</h5>
<h5>#2 YOLOv4 Tiny modelinin tanıtılması ve parametrelerinin girilmesi.</h5>
<h5>#3 Video kaynağının tanıtılması ve sonuç kaydı için VideoWriter nesnesinin tanıtılması.</h5>
<h5>#4</h5> <h5>Tespit yapılacak döngünün başlatılması.</h5>
<h5>#5</h5> <h5>Her bir karede çukur tespiti yapılması ve tespit edilen çukurların koordinatlarının metin dosyasına kaydedilmesi.</h5>
<h5>#6</h5> <h5>Tespit edilen çukurların karelerinin görüntülerinin kaydedilmesi.</h5>
<h5>#7</h5> <h5>FPS değerinin hesaplanması ve ekrana yazdırılması.</h5>
<h5>#8</h5> <h5>Sonuçların ekrana ve video kaydına yazdırılması.</h5>

Kod, "project_files" klasöründe "yolov4_tiny.weights" ve "yolov4_tiny.cfg" dosyalarını kullanıyor. Ayrıca, "geocoder" kütüphanesi de kullanılıyor. Tespit edilen çukurların koordinatları "pothole_coordinates" klasöründe saklanıyor ve görüntüler "pothole_coordinates" klasörüne kaydediliyor.


<h3># Çukur Tespiti Projesi</h3>
Bu proje, bir video kaynağındaki çukurları tespit etmek ve bunların koordinatlarını kaydetmek için bir görüntü işleme uygulamasıdır. YOLOv4 Tiny modeli kullanılarak çukur tespiti yapılmakta ve tespit edilen çukurların koordinatları bir metin dosyasında saklanmaktadır.

<h3># Kullanılan Kütüphaneler</h3>
cv2
geocoder
time
os

<h3># Kullanılan Dosyalar</h3>
yolov4_tiny.weights
yolov4_tiny.cfg
obj.names

<h3># Nasıl Kullanılır?</h3>
Yukarıdaki kütüphaneleri ve dosyaları indirin ve projenin bulunduğu klasöre yerleştirin.
Video kaynağını "test-karsiyaka.mp4" olarak değiştirin veya kendi videonuzu kullanın.
Proje dosyasını çalıştırın.
Çukurların tespit edildiği karelerin görüntüleri "pothole_coordinates" klasöründe kaydedilecektir. Ayrıca, her çukurun koordinatları "coordinates.txt" dosyasına da yazdırılacaktır. Bu dosyada, her çukurun koordinatları ayrı bir satırda listelenir.

<h1>deneme</h1>
<h2>deneme</h2>
<h3>deneme</h3>
<h4>deneme</h4>
<h5>deneme</h5>
