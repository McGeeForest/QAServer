<template>
    <div >
        <h1><i class="ni ni-hat-3"/> HNS-EREC:基于问答语义匹配的问答社区专家推荐方法</h1>
        <div class="row" style="padding:20px">
            <div class="col-6">
                <h4>1.HNS-EREC 模型结构设计</h4>
                <img src="./myimg/hnserecModel.png" alt="" style="width:80%;margin-left:10%">
                <p class="description" style="text-align:center">HNS-EREC 模型结构图</p>
                <p>由于专家用户的活跃度不一，传统方法将专家作为分类标签。这种方法存在专家回答数量分布不平衡现象突出，即前面说明的第一类不平衡现象，影响模型的学习效果。并且，对于新问题进行专家推荐，需要实现基于历史数据的训练对未来新问题的推荐预测。历史问答数据中包含回答信息，但是新问题并不包含回答信息，这种训练输入数据与预测输入数据之间的不一致性会影响模型的专家推荐。</p>
                <p>为了解决遇到的上述问题，我们提出一种History-Now联合问答语义的专家推荐模型（History-Now Q&A Semantics Expert Recommendation Model, HNS-EREC），模型不以专家作为分类标签而是以问答反馈评价作为预测输出。Now模型学习问题和回答之间的语义匹配关系；History模型学习专家用户对问题回答质量预测。History模型的中间输出将基于Now模型的问答语义信息进行调整，将学习到的问题回答之间的语义匹配关系融合到History模型中。最终在新问题的专家推荐上，我们只使用History模型进行预测。History-Now联合问答语义专家推荐模型将专家历史回答作为专家特征作为输入，预测专家对新问题的回答质量，可以避免不均衡数据对模型推荐效果的消极影响。</p>
                <p>模型结构如图4-2所示，其中在Now模型，使用问题和回答作为输入；在History模型，使用问题和专家用户在该问题之前的历史回答作为输入。Now模型预测问答对的语义匹配关系分类标签，History模型预测专家的回答问题的能力。</p>
                <hr/>

            </div>
            <div class="col-6">
                <h4>2.启发式自动采样策略</h4>
                <img src="./myimg/hnserecLabel.png" alt="" style="width:100%;margin-left:0%">
                <p class="description" style="text-align:center">HNS-EREC 启发式自动采样策略</p>
                <p>（1）正样本A（Positive samples A）：对于一个给定的问题q1，我们将其与它的最佳答案配对，并将这个问题-答案对标记为正样本A。</p>
                <p>（2）正样本B（Positive samples B）：对于一个给定的问题q1，我们将其与它的非最佳答案配对，并将这个问题-答案对标记为正样本B。</p>
                <p>（3）负样本C（Negative samples C）：对于一个给定的问题q1，我们选择与其标题相似的问题q2的最佳答案 ，与q1配对，记为负样本C。</p>
                <p>（4）负样本D（Negative samples D）：对于一个给定的问题q1，我们选择与其标题相似的问题q2的非最佳答案 ，与q1配对，记为负样本D。</p>
                <hr/>
                <h4>3.HNS-EREC 损失设计</h4>
                <img src="./myimg/hnserecLoss.png" alt="" style="width:70%;margin-left:0%">
                <p>其中α和λ为预先设置的参数，Θ代表模型的所有参数。</p>
                <p>我们对Now模型和History模型采用联合训练的方式，联合训练两部分模型相比于单独训练Now-Network和History-Network。</p>
                <hr/>
            </div>
        </div>
    </div>
</template>
<script>
export default {
    name: "hnsErec",
}
</script>