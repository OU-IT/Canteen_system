import cv2  
import check_face
import os  

# 初始化摄像头  
cap = cv2.VideoCapture(0)  
  
# 创建窗口  
cv2.namedWindow('Real-time face detection')  
  
while True:  
    # 从摄像头读取一帧图像  
    ret, frame = cap.read()  
  
    # 如果成功读取到一帧图像，ret为True  
    if not ret:  
        print('Exiting ...')  
        break  
  
    # 使用OpenCV的人脸检测器进行人脸检测  
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')  
    faces = face_cascade.detectMultiScale(gray, 1.2, 4)  
  
    # 在检测到的人脸周围画矩形框  
    for (x, y, w, h) in faces:  
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)  
  
    # 显示图像  
    cv2.imshow('Real-time face detection', frame)
    
    if len(faces) > 0:
        filename = os.path.join('.', 'get.jpg')  # get.jpg
        cv2.imwrite(filename, frame)
        uid = check_face.run("get.jpg")
  
    # 按'q'键退出循环  
    if cv2.waitKey(1) & 0xFF == ord('q'):  
        break  
  
# 释放资源并关闭窗口  
cap.release()  
cv2.destroyAllWindows()