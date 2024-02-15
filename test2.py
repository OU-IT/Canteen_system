import cv2  
import os
import time
def run():
    # 创建VideoCapture对象  
    cap = cv2.VideoCapture(0)  
    
    # 创建窗口用于显示摄像头内容  
    cv2.namedWindow('Live Feed', cv2.WINDOW_NORMAL)  
    
    while True:  
        # 从摄像头读取一帧图像  
        ret, frame = cap.read()
        if not ret:  
            break  
    
        # 转换为灰度图像，以减少计算量  
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  
    
        # 加载预训练的人脸检测模型  
        face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')  
    
        # 检测人脸  
        faces = face_cascade.detectMultiScale(gray, 1.1, 4)  
    
        # 在检测到的人脸周围画矩形框  
        for (x, y, w, h) in faces:  
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)  
    
        # 显示图像  
        cv2.imshow('Live Feed', frame)  
        if len(faces) > 0:
            filename = os.path.join('.', 'get.jpg')  # get.jpg
            cv2.imwrite(filename, frame)
            time.sleep(0.2)
    
        # 如果按下'q'键，退出循环  
        if cv2.waitKey(1) & 0xFF == ord('q'):  
            break  
    
    # 释放资源并关闭窗口  
    cap.release()  
    cv2.destroyAllWindows()
run()