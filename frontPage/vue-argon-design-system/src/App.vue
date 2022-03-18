<template>
    <div id="app">
        <router-view name="header"></router-view>
        <main>
            <fade-transition origin="center" mode="out-in" :duration="250">
                <router-view/>
            </fade-transition>
        </main>
        <router-view name="footer"></router-view>
    </div>
</template>
<style>
    .hidden-y::-webkit-scrollbar{
        display:none
    }
    .hidden-y {
        overflow-y: scroll;
        -ms-overflow-style: none;
    }
</style>
<script>
import { FadeTransition } from "vue2-transitions";

export default {
  components: {
    FadeTransition
  },
  methods: {
    
  }
};
</script>
