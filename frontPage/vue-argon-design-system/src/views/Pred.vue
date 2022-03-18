<template>
    <div>
        <div class="position-relative">
            <!-- shape Hero -->
            <section class="section-shaped my-0">
                <div class="shape shape-style-1 shape-default shape-skew">
                </div>
                <div class="container shape-container d-flex">
                    <div class="col px-0">
                        <div class="row" >
                            <div class="col">
                                <h1 class="display-3  text-white">输入问题执行预测</h1>
                                <section class="">
                                    <div class="">
                                        <div class="">
                                            <div class="">
                                                <card gradient="secondary" shadow body-classes="">
                                                    <base-input 
                                                                v-model="questionBody.title"
                                                                class=""
                                                                alternative
                                                                placeholder="问题标题"
                                                                addon-left-icon="ni ni-user-run">
                                                    </base-input>
                                                    <base-input class="">
                                                            <textarea  
                                                                v-model="questionBody.content" 
                                                                class="form-control form-control-alternative" 
                                                                name="name" 
                                                                rows="4"
                                                                cols="80" placeholder="问题内容"></textarea>
                                                    </base-input>
                                                    <base-button v-on:click="uploadQuestion" type="default" round block size="lg" >
                                                        提交问题
                                                    </base-button>
                                                </card>
                                            </div>
                                        </div>
                                    </div>
                                </section>
                            </div>
                            <div class="col hidden-y" style="margin-top: -49px;height:400px;"  >
                                <!-- 右侧专家列表 -->
                                <card v-for="(item, i) in expertList" v-bind:key="i" shadow class="card-profile " style="height:50px;margin-top:5px"  no-body>
                                        <div class="row" style="padding:10px">
                                            <div class="col-sm-8">
                                                <span>用户id：<mark>{{item[0]}}</mark>; {{item[1]}}%</span>
                                            </div>
                                            <div class="col-sm-4" style="width:30%">
                                                <base-button @click="showHistory(item)" size="sm" type="primary" style="float:right;">查看历史</base-button>
                                            </div>                                            
                                        </div>
                                </card>
                            </div>
                        </div>
                    </div>
                </div>
            </section>
            <!-- 1st Hero Variation -->
        </div>
        <modal :show.sync="this.viewHistory" >
            <h4 style="margin-bottom:10px">用户历史回答</h4>
            <div style="height:400px" class="hidden-y">
                <div v-for="(item, index) in historyList" v-bind:key="index">
                    <div class="row">
                        <!-- {{item}} -->
                        <div class="col-2" style="float:left;margin-top:5px">
                            <small style="margin-left:5px">{{formatDate(item[1]*1000)[1]}}</small>
                            <badge type="success">{{formatDate(item[1]*1000)[0]}}</badge>
                        </div>
                        <div style="height:95px" class="hidden-y col-10">
                            <small>{{item[0]}}</small>
                        </div>
                    </div>

                    <hr style="margin-top:3px;margin-bottom:3px">
                </div>
            </div>
            <template slot="footer">
                <base-button type="link" class="ml-auto" @click="viewHistory = false">关闭</base-button>
            </template>
        </modal>
    </div>
</template>

<script>
import modal from "../components/Modal"; 
export default {
  name: "home",
  components: {modal},
  data: function(){
      return {
        questionBody:{
            title:"",
            content:""
        },
        expertList: [],
        viewHistory: false,
        historyList: []
      }

  },
  methods: {
      uploadQuestion: function(){
          console.log(this.questionBody)
          this.$axios.post("/predict", this.questionBody).then(res=>{
              console.log(res.data)
              this.expertList = res.data
          })
      },
      showHistory: function(item){
          console.log("查看用户"+item[0])
          this.$axios.get("/userHistoryById", {params: {
              userId: item[0]
          }}).then(res=>{
              console.log(res)
              this.historyList = res.data
              this.viewHistory=true
              console.log(this.viewHistory)
          })
      }

  }
};
</script>
