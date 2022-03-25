<template>
    <div>
        <section class="section-profile-cover section-shaped my-0">
            <div class="shape shape-style-1 shape-primary shape-skew alpha-4">
            </div>
        </section>
        <!-- <section style="width:80%;margin:auto;margin-top:-200px"> -->
        <section style="width:80%;margin:auto;margin-top:-500px;height:870px">
            <h1 class="display-3  text-white">专家推荐方法展示及社区问答数据分析</h1>
            <tabs fill class="flex-column flex-md-row">
                <card shadow >
                    <tab-pane>
                        <span slot="title">
                            <i class="ni ni-hat-3"> 专家推荐方法展示1：HNS-EREC</i>
                            <!-- <i class="ni ni-cloud-upload-96">专家推荐方法展示1：HNS-EREC</i> -->
                        </span>
                        <hns-erec class=" hidden-y"  style="height:660px"></hns-erec>
                    </tab-pane>

                    <tab-pane title="Profile">
                        <span slot="title">
                            <i class="ni ni-hat-3"> 专家推荐方法展示2：CFF-EREC</i>
                            
                        </span>
                        <cff-erec  class=" hidden-y"  style="height:660px"></cff-erec>
                    </tab-pane>

                    <tab-pane>
                        <span slot="title">
                            <i class="ni ni-badge"> CQA社区问答数据分析</i>
                        </span>
                        <cqa  class=" hidden-y"  style="height:660px"></cqa>
                    </tab-pane>
                </card>
            </tabs>
        </section>
        
    </div>
</template>
<script>
import Tabs from "../components/Tabs/Tabs.vue"
import TabPane from "../components/Tabs/TabPane.vue"
import hnsErec from "./myComponments/Hnserec.vue"
import cffErec from "./myComponments/Cfferec.vue"
import cqa from "./myComponments/Cqa.vue"
export default {
  name: "modelPresentation",
  components: {
    Tabs,
    TabPane,
    hnsErec,
    cffErec,
    cqa
  }
};
</script>
<style>
</style>
