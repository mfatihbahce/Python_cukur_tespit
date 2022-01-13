#gerekli kutuphanelerin import edilmesi
import cv2 as cv
import geocoder
import time
import os

#tespit edilecek nesne isminin obj.names dosyasindan okunmasi
class_name = []
with open(os.path.join("project_files",'obj.names'), 'r') as f:
    class_name = [cname.strip() for cname in f.readlines()]

#modelin tanitilmasi ve model parametrelerinin girilmesi
net1 = cv.dnn.readNet('project_files/yolov4_tiny.weights', 'project_files/yolov4_tiny.cfg')
net1.setPreferableBackend(cv.dnn.DNN_BACKEND_CUDA)
net1.setPreferableTarget(cv.dnn.DNN_TARGET_CUDA_FP16)
model1 = cv.dnn_DetectionModel(net1)
model1.setInputParams(size=(640, 640), scale=1/255, swapRB=True)

#video kaynaginin tanitilmasi
#parantezin ici 0 olursa kameradan, tirnak isaretleri icinde video ismi yazilirsa videodan tespit edilir
cap = cv.VideoCapture("test-karsiyaka.mp4") 
width  = cap.get(3)
height = cap.get(4)
result = cv.VideoWriter('result.avi', 
                         cv.VideoWriter_fourcc(*'MJPG'),
                         10,(640,480))
#sonuc kaydi ve koordinat alimi gibi islemler icin parametre girilmesi
#script icindeki bazi degiskenlerin baslangic degerlerinin girilmesi
g = geocoder.ip('me')
result_path = "pothole_coordinates"
starting_time = time.time()
Conf_threshold = 0.5
NMS_threshold = 0.4
frame_counter = 0
i = 0
b = 0

#tespit gerceklestigi döngü
while True:
    ret, frame = cap.read()
    frame_counter += 1
    if ret == False:
        break
    #ggörüntünün modele dayali incelenmesi
    classes, scores, boxes = model1.detect(frame, Conf_threshold, NMS_threshold)
    for (classid, score, box) in zip(classes, scores, boxes):
        label = "pothole"
        x, y, w, h = box
        recarea = w*h
        area = width*height
        #tespit sartlarini saglayan cukurlara tespit dörtgeni cizilmesi ve fotograf ile koordinat txt dosyasinin kaydedilmesi
        if(len(scores)!=0 and scores[0]>=0.7):
            if((recarea/area)<=0.1 and box[1]<600):
                cv.rectangle(frame, (x, y), (x + w, y + h), (0,255,0), 1)
                cv.putText(frame, "%" + str(scores[0]*100) + " " + label, (box[0], box[1]-10),cv.FONT_HERSHEY_COMPLEX, 0.5, (255,0,0), 1)
                if(i==0):
                    cv.imwrite(os.path.join(result_path,'pothole'+str(i)+'.jpg'), frame)
                    with open(os.path.join(result_path,'pothole'+str(i)+'.txt'), 'w') as f:
                        f.write(str(g.latlng))
                        i=i+1
                if(i!=0):
                    if((time.time()-b)>=2):
                        cv.imwrite(os.path.join(result_path,'pothole'+str(i)+'.jpg'), frame)
                        with open(os.path.join(result_path,'pothole'+str(i)+'.txt'), 'w') as f:
                            f.write(str(g.latlng))
                            b = time.time()
                            i = i+1
    #ekrana fps yazdirilmasi
    endingTime = time.time() - starting_time
    fps = frame_counter/endingTime
    cv.putText(frame, f'FPS: {fps}', (20, 50),
               cv.FONT_HERSHEY_COMPLEX, 0.7, (0, 255, 0), 2)
    #sonucun ekrana basilmasi ve videonun kaydedilmesi
    #kameradan tespitte videoyu anlik kaydeder, videodan tespitte kayit icin video bitmeden kapatilmamasi gerekir
    cv.imshow('frame', frame)
    result.write(frame)
    key = cv.waitKey(1)
    if key == ord('q'):
        break
    
#son
cap.release()
result.release()
cv.destroyAllWindows()
