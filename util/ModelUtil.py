import torch
from torch.nn.utils.rnn import pad_sequence

def getVecALBert(sentence, tokenizer, model, device):
    token_vecs = []
    with torch.no_grad():  # 不生成计算图，不需要反馈，这样速度更快
        input_ids = torch.tensor(tokenizer.encode(sentence))[:512].unsqueeze(0).to(device, non_blocking=True)
        # last_hidden_state = model(input_ids).last_hidden_state.squeeze(0)
        out = model(input_ids)[0].squeeze(0)
    # return last_hidden_state.cpu().numpy().tolist()
    return out.cpu().numpy().tolist()
def excutALBert(texts, tokenizer, model, sen_tokenizer, device):
    res_vec = []
    seq_len = []
    for text in texts:
        # print(text)
        text = str(text).lower()  # 将所有大写字母转换为小写字母
        item_vec = getVecALBert(text, tokenizer, model, device)
        # item_vec = bc(text)
        res_vec.append(item_vec)
        seq_len.append(len(item_vec))
    res_vec = pad_sequence([torch.FloatTensor(item) for item in res_vec], batch_first=True)
    return res_vec, seq_len






