#gerekli kutuphanelerin import edilmesi
import cv2

#resmin okunmasi
img = cv2.imread("test5.jpg") #tirnak isaretleri icine resmin adi yazilir

#tespit edilecek nesne isminin obj.names dosyasindan okunmasi 
with open('obj.names', 'r') as f:
    classes = f.read().splitlines()

#modelin tanitilmasi
net = cv2.dnn.readNetFromDarknet('pothole-yolov3-tiny.cfg', 'pothole-yolov3-tiny.weights')
model = cv2.dnn_DetectionModel(net)
model.setInputParams(scale=1 / 255, size=(416, 416), swapRB=True)
classIds, scores, boxes = model.detect(img, confThreshold=0.6, nmsThreshold=0.4)

#tespit 
for (classId, score, box) in zip(classIds, scores, boxes):
    cv2.rectangle(img, (box[0], box[1]), (box[0] + box[2], box[1] + box[3]),
                  color=(0, 255, 0), thickness=2)
 
cv2.imshow("pothole",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
