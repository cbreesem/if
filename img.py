# coding:utf-8
# import sys
# reload(sys)
import importlib,sys
importlib.reload(sys)
# sys.setdefaultencoding('utf8')
import cv2
# 待检测的图片路径
imagepath = r'timg6.jpeg'
# 获取训练好的人脸的参数数据，这里直接从GitHub上使用默认值
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default1.xml')

# 读取图片

image = cv2.imread(imagepath)
gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

# 探测图片中的人脸
# minSize=(int(w/divisor), int(h/divisor))#这里加了一个取整函数
# minSize=(800, 600) #这里加了一个取整函数
# faces = face_cascade.detectMultiScale(gray, 1.2, 2, cv2.CASCADE_SCALE_IMAGE,minSize) #人脸检测

faces = face_cascade.detectMultiScale(
    gray,
    scaleFactor = 1.15,
    minNeighbors = 5,
    minSize = (370,220),
    flags = cv2.CASCADE_SCALE_IMAGE
)

print ("发现%s个人脸!" % len(faces))

for(x,y,w,h) in faces:
    # cv2.rectangle(image,(x,y),(x+w,y+w),(0,255,0),2)
    cv2.circle(image,((x+x+w)/2,(y+y+h)/2),w/2,(0,255,0),2)

cv2.imshow("Find Faces!",image)

cv2.waitKey(0)
