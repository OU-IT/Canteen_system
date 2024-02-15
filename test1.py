import wx
import key
import check_face
import pay
import get_rest_moeny
import cv2  
import os 
import bp_pred

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
    
    # 初始化摄像头
    # bp_pred.run("s12")  
    cap = cv2.VideoCapture(0)  
  
    # 创建窗口  
    cv2.namedWindow('t')  
  
    # GUI应用程序和窗口对象  
    app = wx.App()  
    my_frame = MyFrame()  
  
    # 标志变量，控制是否显示GUI窗口  
    show_gui = False  
  
    while True:  
        # 从摄像头读取一帧图像  
        ret, frame = cap.read()  
          
        if not ret:  
            print('Exiting ...')  
            break  
  
        # 使用OpenCV的人脸检测器进行人脸检测  
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  
        face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')  
        faces = face_cascade.detectMultiScale(gray, 1.2, 4)  
  
        # 在检测到的人脸周围画矩形框  
        for (x, y, w, h) in faces:  
            cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)  
  
        # 显示图像  
        cv2.imshow('t', frame)  
  
        # 如果检测到人脸并且GUI窗口还没有显示，则显示 
        if len(faces) > 0 and not show_gui:  
            filename = os.path.join('.', 'get.jpg')  # get.jpg  
            cv2.imwrite(filename, frame)  
            uid = "s0"
            uid = check_face.run("get.jpg")  # 处理图片返回信息  
            show_gui = True  
            my_frame.Show()
        # show_gui = True  
        # my_frame.Show()
        if len(faces) > 0:
            filename = os.path.join('.', 'get.jpg')  # get.jpg  
            cv2.imwrite(filename, frame)  
            uid = "s0"
            uid = check_face.run("get.jpg")
            bp_pred.run(uid) 
  
    # 释放资源并关闭窗口  
    cap.release()  
    cv2.destroyAllWindows()  
  
    # 如果GUI窗口已经显示，则在关闭OpenCV窗口后继续运行GUI事件循环  
    if show_gui:  
        app.MainLoop()