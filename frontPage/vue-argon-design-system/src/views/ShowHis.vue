<template>
    <div class="">
        <section class="section-profile-cover section-shaped my-0">
            <div class="shape shape-style-1 shape-primary shape-skew alpha-4">
            </div>
        </section>
        <section class="" style="margin-top: -500px;margin-left:200px">
            <h1 class="display-3  text-white" style="margin-top: -100px">用户历史查询</h1>
            <card  style="width:1000px;height:500px"  no-body>
                <div class="col-12" style="flex:0 0 10%;">
                    <badge class="col-2" tag="a" href="#" type="secondary" style="height:30px">用户ID</badge>
                    <badge class="col-9" tag="a" href="#" type="secondary" style="height:30px">历史表现</badge>
                </div>
                <div class="row" >
                    <div class="col-2 hidden-y" style="margin-left:20px;height:460px" >
                        <div
                            v-for="(item,i) in this.userList" v-bind:key="i"  
                            @click="showHistoryWithQuestion(item)">
                            <badge tag="a" href="#" type="default" class="col-12">{{item}}</badge><br/>
                        </div>
                    </div>

                    <div class="col-9 hidden-y"  style="height:460px">
                        <div v-for="(item,i) in this.userHistoryWithQuestion" v-bind:key="i">
                            <div >
                                <strong>question content:</strong><br/>
                                <small>{{item[0]}}</small>
                                <br/><br/><strong>answered by user at  <mark>{{formatDate_use(item[2]*1000)[0]}} {{formatDate_use(item[2]*1000)[1]}}</mark></strong><br/>
                                <small>{{item[1]}}</small>
                                <hr/>
                            </div>
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
            userHistoryWithQuestion: []
        }
    },
    mounted (){
      console.log("创建完成");
      this.$axios.get("/userList").then(res=>{
          console.log(res)
          this.userList = res.data
      })
  },
  methods: {
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
