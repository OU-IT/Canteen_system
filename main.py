import wx
import key
import check_face
import pay
import get_rest_moeny
import cv2  
import os 
import bp_pred
import threading
from wx.lib.pubsub import pub

c1p = 1
c2p = 2
c3p = 3
c4p = 4
num = 0
a1 ,a2 ,a3 ,a4 ,n1, n2, n3, n4 = 0, 0, 0, 0, 0, 0, 0, 0


class MyFrame(wx.Frame):
    def __init__(self, parent=None, title="点餐"):
        super(MyFrame, self).__init__(parent, title=title)
        self.init_ui()

    def init_ui(self):

        global c1p,c2p,c3p,c4p

        self.set_size((350, 250))
        panel = wx.Panel(self)
        sizer = wx.GridBagSizer(hgap=20, vgap=20)

        # 创建4个按钮和合计标签
        button1 = wx.Button(panel, label="菜1," + str(c1p) + "元",size=(120, 50))
        button2 = wx.Button(panel, label="菜2," + str(c2p) + "元",size=(120, 50))
        button3 = wx.Button(panel, label="菜3," + str(c3p) + "元",size=(120, 50))
        button4 = wx.Button(panel, label="菜4," + str(c4p) + "元",size=(120, 50))
        button5 = wx.Button(panel, label="支付",size=(120, 50))
        self.total_label = wx.StaticText(panel, label="")

        sizer.Add(button1, pos=(0, 0))
        sizer.Add(button2, pos=(0, 1))
        sizer.Add(button3, pos=(1, 0))
        sizer.Add(button4, pos=(1, 1))
        sizer.Add(button5, pos=(2, 0), flag=wx.ALIGN_CENTER_VERTICAL)
        sizer.Add(self.total_label, pos=(2, 1), flag=wx.ALIGN_CENTER_VERTICAL)


        button1.Bind(wx.EVT_BUTTON, self.on_button1_click)
        button2.Bind(wx.EVT_BUTTON, self.on_button2_click)
        button3.Bind(wx.EVT_BUTTON, self.on_button3_click)
        button4.Bind(wx.EVT_BUTTON, self.on_button4_click)
        button5.Bind(wx.EVT_BUTTON, self.on_button5_click)

        panel.SetSizer(sizer)

    def on_button1_click(self, event):
        global num, n1, n2, n3, n4 ,a1 ,a2 ,a3 ,a4
        try:
            key.numz = ""
            key.run()
            a1 = int(key.numz)
            if a1 is not None:
                n1 = c1p * a1
                num = n1 + n2 + n3 + n4
                self.total_label.SetLabel("合计：" + str(num))
        except Exception as e:
            print("菜1计算错误:", e)

    def on_button2_click(self, event):
        global num, n1, n2, n3, n4, a1 ,a2 ,a3 ,a4
        try:
            key.numz = ""
            key.run()
            a2 = int(key.numz)
            if a2 is not None:
                n2 = c2p * a2
                num = n1 + n2 + n3 + n4
                self.total_label.SetLabel("合计：" + str(num))
        except Exception as e:
            print("菜2计算错误:", e)

    def on_button3_click(self, event):
        global num, n1, n2, n3, n4, a1 ,a2 ,a3 ,a4
        try:
            key.numz = ""
            key.run()
            a3 = int(key.numz)
            if a3 is not None:
                n3 = c3p * a3
                num = n1 + n2 + n3 + n4
                self.total_label.SetLabel("合计：" + str(num))
        except Exception as e:
            print("菜3计算错误:", e)

    def on_button4_click(self, event):
        global num, n1, n2, n3, n4, a1 ,a2 ,a3 ,a4
        try:
            key.numz = ""
            key.run()
            a4 = int(key.numz)
            if a4 is not None:
                n4 = c4p * a4
                num = n1 + n2 + n3 + n4
                self.total_label.SetLabel("合计：" + str(num))
        except Exception as e:
            print("菜4计算错误:", e)

    def on_button5_click(self, event):
        global num, n1, n2, n3, n4, a1 ,a2 ,a3 ,a4
        num = n1 + n2 + n3 + n4
        self.total_label.SetLabel("合计：" + str(num))
        uid = check_face.run("get.jpg")#通过人脸获取学号
        Moeny_enough = pay.run(uid,num,a1,a2,a3,a4)#返回是否够钱，够钱就pay
        num, n1, n2, n3, n4 = 0,0,0,0,0
        self.total_label.SetLabel("合计：" + str(num))
        if Moeny_enough==0: #不够钱
            print("余额不足余额不足余额不足余额不足")
            self.total_label.SetLabel("余额不足," + "余额:" + str(get_rest_moeny.run(uid)))
            num, n1, n2, n3, n4, uid = 0,0,0,0,0,"s0"
        else:
            self.total_label.SetLabel("消费成功," + "余额:" + str(get_rest_moeny.run(uid)))
            uid = "s0"

    def set_size(self, size):
        self.SetSize(size)
        self.Center()


if __name__ == "__main__":
    
    # 摄像头处理线程  
    def camera_thread():  
        global cap  
        
        while True:  
            ret, frame = cap.read()  
            if not ret:  
                print('Exiting ...')
                break  
            
            # 人脸检测  
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  
            face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')  
            faces = face_cascade.detectMultiScale(gray, 1.2, 4)  
            
            # 检测到人脸时发送消息给GUI线程  
            if len(faces) > 0:  
                pub.sendMessage('face_detected', frame=frame) 
            
            # 显示图像  
            cv2.imshow('Camera Feed', frame)  
            
            # 按'q'键退出循环  
            if cv2.waitKey(1) & 0xFF == ord('q'):  
                break  
        
        # 释放摄像头资源  
        cap.release()  
        cv2.destroyAllWindows()  
    
    # GUI线程中的事件处理函数  
    def on_face_detected(frame):  
        # 这里可以更新GUI，例如显示图片或处理图片  
        # 这里的操作应该尽快完成，避免阻塞GUI线程
        filename = os.path.join('.', 'get.jpg')  
        cv2.imwrite(filename, frame)  
        uid = "s0"  
        uid = check_face.run("get.jpg")
        # 处理图片返回信息  
        bp_pred.run(uid)  
    
    # 初始化pubsub  
    pub.subscribe(on_face_detected, 'face_detected')  
    
    # 创建并显示GUI窗口  
    app = wx.App()  
    my_frame = MyFrame()  
    my_frame.Show()  
    
    # 初始化摄像头  
    cap = cv2.VideoCapture(0)  
    
    # 启动摄像头处理线程  
    camera_thread_task = threading.Thread(target=camera_thread)  
    camera_thread_task.start()  
    
    # 运行GUI事件循环  
    app.MainLoop()  
    
    # 确保在退出前等待摄像头线程结束  
    camera_thread_task.join()