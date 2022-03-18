from tkinter import E
import torch
import nltk
import pandas as pd
import _thread
from nltk.tokenize import sent_tokenize
from transformers import AlbertModel, AlbertTokenizer
from model import Sou1Model
from util import ModelUtil as modelUtil
class ModelService():
    def __init__(self, modelPath, dataService):
        src = '/home/zsl/projects/project/QAData/'
        device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
        # 创建参数列表：
        param = {}
        param['device'] = str(device)
        param['batch_size'] = 1
        param['learningrate'] = 0.01
        param['extracter_name'] = "CNNTextExtracterWithMHSelfAttion"
        param['extracter_kernel_num'] = 300
        param['extracter_kernel_size'] = 3
        param['extracter_vocab_size'] = 1000
        param['extracter_embed_dim'] = 768
        param['extracter_padding'] = 0
        param['extracter_n_hidden'] = 150
        param['extracter_out_dim'] = 400
        param['MFC1_hidden'] = 200
        param['MFC1_out'] = 2
        param['dropout'] = 0.5
        schedulerDict = {}
        schedulerDict['name'] = "StepLR"
        schedulerDict['optimizer'] = "SGD"
        schedulerDict['lr'] = param['learningrate']  # 不要修改此值，对上面的学习率修改
        schedulerDict['step_size'] = 300
        schedulerDict['gamma'] = 0.85
        param['optimizer'] = schedulerDict
        param['MFC2_hidden'] = 50
        model = Sou1Model.Sou1M(param, device)
        modelWeights = torch.load(modelPath)
        model.load_state_dict(modelWeights)
        self.dataService = dataService
        self.device = device
        self.param = param
        self.model = model.to(device, non_blocking=True)
        self.bertTokenizer = AlbertTokenizer.from_pretrained('albert-base-v2')
        self.bertModel = AlbertModel.from_pretrained('albert-base-v2').to(device, non_blocking=True)
        self.sen_tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')   #加载punkt句子分割器
        # sourceNetwork的更新与TargetNetwork的优化器一致，初始值也相同     
        print(" *** 模型及优化器初始化完成")
    
    def pred(self, q_text_batch, u_his_batch):
        data = "run predict."
        q_vec_batch, q_real_len = modelUtil.excutALBert(q_text_batch, self.bertTokenizer, self.bertModel, self.sen_tokenizer, self.device)
        u_his_vec_batch, u_his_real_len = modelUtil.excutALBert(u_his_batch, self.bertTokenizer, self.bertModel, self.sen_tokenizer, self.device)
        q_real_len = torch.Tensor(q_real_len) # 代表每个句子的长度
        u_his_real_len = torch.Tensor(u_his_real_len) # 代表每个句子的长度
        qu_represent, RS = self.model.forward(q_vec_batch.to(self.device), u_his_vec_batch.to(self.device), q_real_len, u_his_real_len)
        prob = torch.softmax(RS, dim=1)
        # print(data)
        return prob
    
    def getExperts(self, qText, userList):
        probList=[]
        for userId in userList:
            try:
                prob = self.pred([qText], [self.dataService.getHistoryByUserId(userId)])
                probList.append(prob.cpu().detach().numpy()[0][0])
            except Exception:
                print("Exception")
            # print(prob.cpu().detach().numpy()[0][0])
        # predExperts['userId']=userList
        # predExperts['prob']=probList
        return userList, probList
        topExperts = predExperts.sort_values(by='prob', ascending=False).head(10)
        print(topExperts)
        return[9656320, 1830916, 5210117, 1712135, 571407, 5285908, 1206301, 5914654]
    
    def getExpertsThreading(self, qText, userList):
        predExperts = pd.DataFrame()
        probList=[]
        userList, probList = self.getExperts(qText, userList)
        predExperts['userId']=userList
        predExperts['prob']=probList
        topExperts = predExperts.sort_values(by='prob', ascending=False).head(10)
        print(topExperts)
        return [[str(row['userId']), format(row['prob']*100,'.2f')] for index, row in topExperts.iterrows()]

