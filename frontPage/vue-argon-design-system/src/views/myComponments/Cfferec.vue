<template>
    <div >
        <h1><i class="ni ni-hat-3"/> CFF-EREC:基于粗细粒度特征融合的问答社区专家推荐方法</h1>
        <div class="row" style="padding:20px">
            <div class="col-6">
                <h4>1.CFF-EREC 模型结构设计</h4>
                <img src="./myimg/cfferecModel.png" alt="" style="width:80%;margin-left:10%">
                <p class="description" style="text-align:center">CFF-EREC 模型结构图</p>
                <p>传统的专家推荐算法大多采用专家资料构建专家特征，但专家资料存在更新不及时等问题，无法准确的描述专家特征。因此我们通过专家回答过的历史问题来构建专家特征，问题主要由问题文本t和问题标签l构成。</p>
                <p>想要建模问题特征，如果只通过问题标签构建问题特征，则存在特征单一，无法准确的建模问题；如果只通过问题文本进行问题特征构建，则问题标签这种粗粒度特征无法充分利用。</p>
                <p>所以，对于问题特征，我们选择基于问题文本提取细粒度特征，基于问题标签构建粗粒度特征，通过模型将两类特征融合，构建问题特征。在问题特征构建准确的基础之上，我们可以基于用户历史回答的问题准确的构建专家特征。</p>
                <hr/>

            </div>
            <div class="col-6">
                <h4>2.粗细粒度特征融合单元CFU</h4>
                <img src="./myimg/cfferecCfu.png" alt="" style="width:100%;margin-left:0%">
                <p class="description" style="text-align:center">图 粗细粒度特征融合单元CFU的结构</p>
                <p>对于问题特征，我们设计了粗细粒度特征融合单元（Coarse and Fine-granularity Feature Fusion Unit，CFU），将不同粒度的特征进行融合。对于专家特征，则基于历史回答的问题特征的平均构建。在匹配预测层，首先将新问题特征qu与专家特征eu相结合，共同传入多层感知器，计算样本《q，u》在两类标签（正、负）上的概率。</p>
                <hr/>
            </div>
        </div>
    </div>
</template>
<script>
export default {
    name: "cffErec",
}
</script>