from urllib import request
from flask import Flask, request
from flask_cors import cross_origin
from app.DataRun import DataService
from app.ModelRun import ModelService
from util import Message as Message
import sys, os
os.environ["KMP_DUPLICATE_LIB_OK"]="TRUE"
app = Flask(__name__)
run_os = "3090"
basePath = ""
if run_os == "win10":
    basePath = "D:/OneDriveEdu/file/project2/QAData/"
elif run_os == "3090":
    basePath = "/home/zsl/projects/project/QAServer/"
else:
    basePath = "/home/student/zoushulin/project/QAServer/"

# Service&Bean 初始化
dataService = DataService(basePath + "/data/")
modelService = ModelService(basePath + '/model/weight/trainSouModel_step_5,acc_0.7.pth', dataService)
messageBean = Message.Msg()


@app.route('/')
@cross_origin()
def hello_world():
    return 'hello world'

# 输入一个问题返回预测的专家列表
@app.route('/predict', methods=['GET', 'POST'])
@cross_origin()
def predict():
    # return messageBean.setSuccessMsg(modelService.pred()).toJson()
    if request.method=='POST':
        qText = request.form['title'] + "." + request.form['content']
        return messageBean.setSuccessMsg(modelService.getExpertsThreading(qText, dataService.userList))
    return ""

# 获取用户全部回答历史
@app.route("/userHistory", methods=['GET', 'POST'])
@cross_origin()
def userHistory():
    return messageBean.setSuccessMsg(dataService.allUserHistory)

# 通过用户ID获取用户回答历史
@app.route("/userHistoryById", methods=['GET', 'POST'])
@cross_origin()
def userHistoryById():
    if(request.method=='GET'):
        return messageBean.setSuccessMsg(dataService.getHistoryByUserId(request.args.get('userId')))
    else:
        return messageBean.setSuccessMsg(dataService.getHistoryByUserId(dataService.userList[0]))

# 根据id获取用户回答历史以及问题和评分内容
@app.route("/getUserHistoryWithQuestion", methods=['GET', 'POST'])
@cross_origin()
def getHistoryWithQuestion():
    if(request.method=='GET'):
        return messageBean.setSuccessMsg(dataService.getHistoryByUserIdWithQuestion(request.args.get('userId')))
    else:
        return messageBean.setSuccessMsg(dataService.getHistoryByUserIdWithQuestion(dataService.userList[0]))


# 获取用户列表
@app.route("/userList", methods=['GET', 'POST'])
@cross_origin()
def userList():
    return messageBean.setSuccessMsg(dataService.userList)


if __name__ == '__main__':
    app.run(host='0.0.0.0',port=7526, debug=True)