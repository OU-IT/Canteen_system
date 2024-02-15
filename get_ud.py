import pandas as pd  
import mysql.connector  
  
# 创建数据库连接
def run(uid):  
    conn = mysql.connector.connect(  
        host="localhost",   
        user="root",  
        password="root", 
        database="dish" 
    )  
    
    # 创建游标对象  
    cursor = conn.cursor()  
    
    # 查询所有记录，并按日期分组对d1、d2、d3、d4进行求和  
    query = f"""    
    SELECT SUM(d1) AS d1n, SUM(d2) AS d2n, SUM(d3) AS d3n, SUM(d4) AS d4n    
    FROM {uid}  
    """ 
    cursor.execute(query)  
    
    # 将结果转换为pandas DataFrame  
    results = pd.DataFrame(cursor.fetchall(), columns=["d1n", "d2n", "d3n", "d4n"])  
    
    # 关闭游标和连接  
    cursor.close()  
    conn.close()  

    d1n = int(results['d1n'].iloc[0])  
    d2n = int(results['d2n'].iloc[0])  
    d3n = int(results['d3n'].iloc[0])  
    d4n = int(results['d4n'].iloc[0])

    return d1n,d2n,d3n,d4n
    
    # # 显示结果  
    # print(d1n)