# 定义返回格式 状态码code 备注remark 数据data
import json
class Msg():
    def __init__(self) -> None:
        self.code=""
        self.remark=""
        self.data=""
    def setSuccessMsg(self, dataContent):
        self.code=0
        self.remark="任务执行完成"
        self.data=dataContent
        return self.toJson()
    def toJson(self):
        res = {}
        res["code"] = self.code
        res["remark"] = self.remark
        res["data"] = self.data
        
        return res
