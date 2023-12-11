import csv
import pandas as pd
def isMember(stuID):

    # 檔案路徑
    file_path = 'static/data/member.csv'

    # 開啟CSV檔案
    with open(file_path, 'r') as file:
        # 創建CSV讀取器
        csv_reader = csv.reader(file)
        
        # 迭代每一列
        for row in csv_reader:
            # row是一個列表，包含該列的所有值
            if str(stuID) in row:
                return True,row[3]
    return False
            

def Buy(stuID, Name):
    # 讀取現有的CSV文件（如果存在），或者創建一個新的DataFrame
    try:
        df = pd.read_csv('static/data/alreadyBought.csv')
    except FileNotFoundError:
        df = pd.DataFrame(columns=['班級','學號', '姓名'])

    # 創建新的一行數據
    new_data = {'班級':"" ,'學號': stuID, '姓名': Name}

    # 將新數據追加到DataFrame
    df = pd.concat([df, pd.DataFrame([new_data])], ignore_index=True)

    # 寫入CSV文件
    df.to_csv('static/data/alreadyBought.csv', index=False)

def isBought(stuID):
    # 檔案路徑
    file_path = 'static/data/alreadyBought.csv'

    # 開啟CSV檔案
    with open(file_path, 'r') as file:
        # 創建CSV讀取器
        csv_reader = csv.reader(file)
        
        # 迭代每一列
        for row in csv_reader:
            # row是一個列表，包含該列的所有值
            if str(stuID) in row:
                return True
    return False

def getBoughtList():
    # 檔案路徑
    file_path = 'static/data/alreadyBought.csv'
    result = []
    # 開啟CSV檔案
    with open(file_path, 'r') as file:
        # 創建CSV讀取器
        csv_reader = csv.reader(file)
        
        # 迭代每一列
        for row in csv_reader:
            # row是一個列表，包含該列的所有值
            result.append(row)
    return result

