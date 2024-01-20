import cv2

img = cv2.imread("C:/Users/Gurjas/Desktop/PRO-C106-Student-Boilerplate-main/WIN_20231224_12_23_36_Pro.jpg")

gray= cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

face_cascade = cv2.CascadeClassifier('C:/Users/Gurjas/Desktop/PRO-C106-Student-Boilerplate-main/haarcascade_frontalface_default.xml')

faces = face_cascade.detectMultiScale(gray)
print(faces)

for (x,y,w,h) in faces:
       cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
             
cv2.imshow('img',img)
cv2.waitKey(0)



