import Vue from 'vue'
import Router from 'vue-router'
import MyPathways from './components/MyPathways.vue'
import ExpansionPanel from './components/ExpansionPanel.vue'
import ExplorePathways from './components/ExplorePathways.vue'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: "/home",
      name: "home",
      component: ExpansionPanel,
    },
    {
      path: "/activity",
      name: "activity",
      component: MyPathways,
    },
    {
      path: "/explore",
      name: "explore",
      component: ExplorePathways,
    },
    {
      path: "*",
      name: "",
      component: ExpansionPanel
    }
  ],
  mode: "history",
});
