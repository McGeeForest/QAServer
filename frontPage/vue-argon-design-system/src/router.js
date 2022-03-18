import Vue from "vue";
import Router from "vue-router";
import AppHeader from "./layout/AppHeader";
import Pred from "./views/Pred.vue";
import ShowHis from "./views/ShowHis.vue";
import Start from "./views/Starter.vue";

Vue.use(Router);

export default new Router({
  linkExactActiveClass: "active",
  routes: [
    {
      path: "/",
      name: "components",
      components: {
        header: AppHeader,
        default: Start
      }
    },
    {
      path: "/pred",
      name: "pred",
      components: {
        header: AppHeader,
        default: Pred
      }
    },
    {
      path: "/showHis",
      name: "showHis",
      components: {
        header: AppHeader,
        default: ShowHis
      }
    }
  ],
  scrollBehavior: to => {
    if (to.hash) {
      return { selector: to.hash };
    } else {
      return { x: 0, y: 0 };
    }
  }
});
