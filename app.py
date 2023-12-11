from flask import Flask, request, jsonify,render_template
from func import *

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/boughtList')
def boughtList():
    return render_template('boughtList.html')

@app.route('/isMember', methods=['POST'])
def is_member():
    # 從前端獲取輸入的學號
    student_id = request.form.get('studentId')
    status = isBought(student_id)
    if status:
        status = '已購票'
    else:
        status = '未購票'
    # 檢查學號是否在會員資料庫中
    if isMember(student_id):
        student_name = isMember(student_id)[1]
        response = {'success': True, 'studentInfo': f'{student_id} - {student_name}', 'status': status , 'studentName': student_name}
    else:
        response = {'success': False}

    # 將回應轉換為JSON格式發送給前端
    return jsonify(response)

@app.route('/buy', methods=['POST'])
def buy():
    # 從前端獲取輸入的學號
    student_id = request.form.get('studentId')
    student_name = request.form.get('studentName')
    if isBought(student_id):
        response = {'success': False}
        return jsonify(response)
    else:
        Buy(student_id, student_name)
        response = {'success': True}
        return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)
