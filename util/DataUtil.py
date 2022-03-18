import pandas as pd
def readQASet(data_path):
    # 1. 读取数据集
    month1 = pd.read_csv(data_path + 'month1.csv')
    month2 = pd.read_csv(data_path + 'month2.csv')
    month3 = pd.read_csv(data_path + 'month3.csv')
    month4 = pd.read_csv(data_path + 'month4.csv')
    month5 = pd.read_csv(data_path + 'month5.csv')
    month6 = pd.read_csv(data_path + 'month6.csv')
    month7 = pd.read_csv(data_path + 'month7.csv')
    month8 = pd.read_csv(data_path + 'month8.csv')
    month9 = pd.read_csv(data_path + 'month9.csv')
    month10 = pd.read_csv(data_path + 'month10.csv')
    month11 = pd.read_csv(data_path + 'month11.csv')
    month12 = pd.read_csv(data_path + 'month12.csv')
    cols = ["q_id", "q_time", "q_text", "u_id", "a_id","a_text","a_time", "r", "score"]
    all_set = pd.concat([
        month1, month2, month3, month4, month5, month6, month7, month8, month9, month10,month11,month12
        ]).drop(columns='Unnamed: 0')[cols].drop_duplicates(subset=None, keep='first', inplace=False)  # 真实问答对与负采样问答对合并 1:1的比例
    # id转为字符串防止类型不匹配
    all_set['q_id']=[str(item) for item in all_set['q_id']]
    all_set['u_id']=[str(item) for item in all_set['u_id']]
    all_set['a_id']=[str(item) for item in all_set['a_id']]
    print(" *** data read over, the length is " + str(len(all_set)))
    return all_set