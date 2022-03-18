<template>
    <div>
        <section class="section-profile-cover section-shaped my-0">
            <div class="shape shape-style-1 shape-primary shape-skew alpha-4">
            </div>
        </section>
        <section style="margin-top: -500px;margin-left:200px">
            <h1 class="display-3  text-white" style="margin-top: -100px">用户历史查询</h1>
            <card :style="contentStyle" no-body>
                <div style="flex:0 0 5%;">
                    <badge class="col-2" tag="a" href="#" type="secondary" style="height:20px">用户ID</badge>
                    <badge class="col-9" tag="a" href="#" type="secondary" style="height:20px">历史表现</badge>
                </div>
                <div class="row" >
                    <div class="col-2 hidden-y" id="select" style="height:600px" >
                        <div
                            v-for="(item,i) in this.userList" v-bind:key="i"  
                            @click="showHistoryWithQuestion(item)">
                            <badge tag="a" href="#" type="default" class="col-12">{{item}}</badge><br/>
                        </div>
                    </div>

                    <div class="col-9 hidden-y"  style="height:80%">
                        <div v-for="(item,i) in this.userHistoryWithQuestion" v-bind:key="i">
                            <strong>question content:</strong><br/>
                            <small>{{item[0]}}</small>
                            <br/><br/><strong>answered by user at <mark>{{formatDate_use(item[2]*1000)[0]}} {{formatDate_use(item[2]*1000)[1]}}</mark></strong><br/>
                            <small>{{item[1]}}</small>
                            <hr/>
                            <!-- <div class="hidden-y" style="height:50px">{{item[1]}}</div> -->
                        </div>
                    </div>
                </div>
            </card>
        </section>
    </div>
</template>
<script>
export default {
    data: function(){
        return {
            userList: [],
            userHistoryWithQuestion: [],
            contentStyle: {
                width: "1000px",
                height: "500px",
                padding: "15px"
            }
        }
    },
    created(){
        window.addEventListener('resize', this.getContentStyle);
        this.getContentStyle()
    },
    mounted (){
      console.log("创建完成");
      this.$axios.get("/userList").then(res=>{
          console.log(res)
          this.userList = res.data
      })
  },
  methods: {
      getContentStyle: function(){
          this.contentStyle.width = document.documentElement.clientWidth*0.8+"px"
          this.contentStyle.height = document.documentElement.clientHeight*0.8+"px"
      },
      showHistoryWithQuestion: function(item){
          console.log(item);
          this.$axios.get("/getUserHistoryWithQuestion", {params: {
              userId: item
          }}).then(res => {
              console.log(res.data)
              this.userHistoryWithQuestion = res.data
          })
      },
      formatDate_use: function(item){
          return this.$FormatDate(item)
      }
  }
};
</script>
<style>
</style>
