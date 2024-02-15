import cv2
import os

def run():
    # 检查摄像头
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("未检测到摄像头")
        exit()

    # 初始
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

    while True:
        # 读取一帧图像
        ret, frame = cap.read()
        if not ret:
            break

            # 灰度
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # 检测人脸
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)

        # 在图像中框出人脸
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

            # 显示图像
        cv2.imshow('frame', frame)

        # q退出
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

            #拍照保存
        if len(faces) > 0:
            filename = os.path.join('.', 'get.jpg')  # get.jpg
            cv2.imwrite(filename, frame)
            break

        # 关闭窗口
    cap.release()
    cv2.destroyAllWindows()

#run()