import Vue from 'vue'
import Router from 'vue-router'
import MyPathways from './components/MyPathways.vue'
import ExpansionPanel from './components/ExpansionPanel.vue'
import ExplorePathways from './components/ExplorePathways.vue'
import ResultingPathways from './components/ResultingPathways.vue'

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
      path: "/result",
      name: "result",
      component: ResultingPathways,
    },
    {
      path: "*",
      name: "",
      component: ExpansionPanel
    }
  ],
  mode: "history",
});
