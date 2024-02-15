import pickle
import get_ud
with open('my_model.pkl', 'rb') as f:  
    pickle.load(f)  
def run(uid):
    if isinstance(uid, type(None)) == 0:
        if int(uid[1:]) > 0:
    # 加载模型  
            d1,d2,d3,d4 = get_ud.run(str(uid))
            with open('my_model.pkl', 'rb') as f:  
                model = pickle.load(f)  
            
            # 数据集X_new，需要进行预测  
            X_new = [[int(uid[1:]), d1, d2, d3, d4]]
            
            # 使用模型进行预测  
            y_pred = model.predict(X_new)  
            
            predn = max(y_pred[0])
            a = 0
            while 1:
                if y_pred[0][a] == predn:
                    print("Maybe you like:"+str(a+1))
                    break
                a+=1
            return a
            
            # 输出预测结果  
            # print(y_pred)
            # print(predn)
# run(27,1,1,1,1)