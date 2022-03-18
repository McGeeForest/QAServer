/*!

=========================================================
* Vue Argon Design System - v1.1.0
=========================================================

* Product Page: https://www.creative-tim.com/product/argon-design-system
* Copyright 2019 Creative Tim (https://www.creative-tim.com)
* Licensed under MIT (https://github.com/creativetimofficial/argon-design-system/blob/master/LICENSE.md)

* Coded by www.creative-tim.com

=========================================================

* The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

*/
import Vue from "vue";
import App from "./App.vue";
import router from "./router";
import Argon from "./plugins/argon-kit";
import './registerServiceWorker'
import axios from 'axios'
Vue.config.productionTip = false;
Vue.use(Argon);
Vue.prototype.$axios=axios
import qs from "qs"
// 添加请求拦截器
axios.interceptors.request.use(function (config) {
  console.log("拦截");
    // 参数格式转换
    if(config.method=="post"){
        config.data = qs.stringify(config.data);
    }
    return config;
}, function (error) {
    // 对请求错误做些什么
    return Promise.reject(error);
});
axios.interceptors.response.use(res => {
  return res.data;
})
// Vue.prototype.HOST='/apis'
axios.defaults.baseURL='http://10.9.20.17:7526/'
new Vue({
  axios,
  router,
  render: h => h(App)
}).$mount("#app");
import FormatDate from './plugins/FormatDate';
Vue.use(FormatDate)