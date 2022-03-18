# 生成所有用户的历史回答记录，返回dict
from select import select
from util import DataUtil
import pandas as pd
import numpy as np
class DataService():
    def __init__(self, data_path):
        self.allQASet = DataUtil.readQASet(data_path)        # 数据集
        self.allUserHistory = self.allQASet.groupby("u_id")  # 所有用户的历史回答
        self.userList = list(set(self.allQASet["u_id"].values.tolist()))    # 用户列表
    
    # 根据用户id返回历史回答
    def getHistoryByUserId(self, userId):
        textList = self.allUserHistory.get_group(userId)["a_text"].to_list()
        timeList = self.allUserHistory.get_group(userId)["a_time"].to_list()
        res=[(textList[i], timeList[i]) for i in range(len(timeList))]
        return res
    
    def getHistoryByUserIdWithQuestion(self, userId):
        qTextList = self.allUserHistory.get_group(userId)["q_text"].to_list()
        aTextList = self.allUserHistory.get_group(userId)["a_text"].to_list()
        timeList = self.allUserHistory.get_group(userId)["a_time"].to_list()
        scoreList = self.allUserHistory.get_group(userId)["score"].to_list()
        res=[(qTextList[i], aTextList[i], timeList[i], scoreList[i]) for i in range(len(timeList))]
        return res

