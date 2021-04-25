import Vue from 'vue'
import App from './App.vue'
import vuetify from './plugins/vuetify';
import router from './router';
import Vuex from 'vuex';
import Toast from "vue-toastification";
import createPersistedState from 'vuex-persistedstate'

import "vue-toastification/dist/index.css";

Vue.use(Toast, {
  transition: "Vue-Toastification__bounce",
  maxToasts: 1,
  newestOnTop: true
});

Vue.use(Vuex)

// this code here is for tracking application state
// application state includes the following
// 1. current state which is comprised of:
    // a. a pathway the user has selected
    // b. first course the user has selected
    // c. second course the user has selected
    // d. third course the user has selected
// 2. a "shopping cart" which is a json object storing the current states the user has saved 
// I'm just going to import the json files in order to make a working prototype
// not sure if this is bad design

import courses from "../../JSONfiles/courses.json"
import pathways from "../../JSONfiles/pathways.json"

const store = new Vuex.Store({
  state: {
    statecourses: courses,
    statepathways: pathways,
    count: 0,
    currentSelection: {
      pathway: null,
      course1: null,
      course2: null,
      course3: null
    },
    editingCourses: false,
    targetEditIndex: -1,
    // shopping cart starts out as an empty object
    // we just copy application states as the user saves them
    shoppingCart: {
      options: []
    },
    current: 1
  },
  plugins: [createPersistedState()],
  mutations: {
    initializeStore(state) {
      if (localStorage.getItem('options')) {
        try {
          state.shoppingCart.options = JSON.parse(localStorage.getItem('options'))
        } catch (e) {
          localStorage.removeItem('options')
        }
      }

      if (localStorage.getItem('count')) {
        console.log(typeof state.count)
        state.count = parseInt (localStorage.getItem('count'))
        console.log(typeof state.count)
      }

      if (localStorage.getItem('pathway')) {
        state.currentSelection.pathway = localStorage.getItem('pathway')
      }

      if (localStorage.getItem('course1') != "null") {
        state.currentSelection.course1 = localStorage.getItem('course1')
      }

      if (localStorage.getItem('course2') != "null") {
        state.currentSelection.course2 = localStorage.getItem('course2')
      }

      if (localStorage.getItem('course3') != "null") {
        state.currentSelection.course3 = localStorage.getItem('course3')
      }
    },
    setSelectedPathway(state, pathwayID) {
      state.currentSelection.pathway = pathwayID;

      // save in localStorage
      localStorage.setItem('pathway', pathwayID)
    },
    setSelectedCourse1(state, course) {
      state.currentSelection.course1 = course;

      // save in localStorage
      localStorage.setItem('course1',  JSON.stringify(course))
    
    },
    setSelectedCourse2(state, course) {
      state.currentSelection.course2 = course;
      // save in localStorage
      localStorage.setItem('course2',  JSON.stringify(course))
    },
    setSelectedCourse3(state, course) {
       state.currentSelection.course3 = course;

      // save in localStorage
      localStorage.setItem('course3',  JSON.stringify(course))
      console.log(localStorage.getItem('course3'))
    },
    saveButton(state) {
      console.log("Saved button")
      state.shoppingCart.options[state.count] = [state.currentSelection.pathway, JSON.parse(localStorage.getItem('course1')), JSON.parse(localStorage.getItem('course2')), JSON.parse(localStorage.getItem('course3'))];
      state.count += 1;
      state.currentSelection.pathway = null;
      state.currentSelection.course1 = null
      state.currentSelection.course2 = null;
      state.currentSelection.course3 = null;
    },
    clearCurrentSelection(state) {
      state.currentSelection = {}
    },
    saveCurrentSelection(state,currentSelection) {
      state.shoppingCart.options[state.count] = currentSelection;
      state.count+=1;
    },
    loadSelection(state, selectionToLoad) {
      state.currentSelection = selectionToLoad;
    },
    incrementCount(state) {
      state.count += 1;
    },
    clear(state) {
      state.shoppingCart.options = []
      state.count = 0

      // save in localStorage
      localStorage.setItem('options', '')
      localStorage.setItem('count', 0)
    },
    removePath(state, i) {
      state.shoppingCart.options.splice(i, 1)
      state.count -=1

      // save in localStorage
      localStorage.setItem('count', state.count)
      localStorage.setItem('options', JSON.stringify(state.shoppingCart.options))
    }
  },
  getters: {
    progressBarStatus(state) {
      // this function returns the number of courses the user has selected (0, 1, 2 or 3)
      // this is intended to be used with our 3 part progress bar
      if(!state.currentSelection.course1) {
        return 0;
      } else if (!state.currentSelection.course2) {
        return 1;
      } else if (!state.currentSelection.course3) {
        return 2;
      } else {
        return 3;
      }
    },
    firstCourse(state) {
      return state.currentSelection.course1;
    },
    secondCourse(state) {
      return state.currentSelection.course2;
    },
    thirdCourse(state) {
      return state.currentSelection.course3;
    },
    pathway(state) {
      return state.currentSelection.pathway;
    },
    getOptionsLength: state => {
      // double check
      if (state.count === state.shoppingCart.options.length){
        return state.count
      } else {
        return state.shoppingCart.options.length;
      }
    },
    getOptions: state => {
      console.log(state)
      return store.state.shoppingCart.options;
    },
  }
})

Vue.config.productionTip = false

new Vue({
  router,
  vuetify,
  store,
  initializeStore() { 
    store.commit('initializeStore'); 
  },
  render: h => h(App)
}).$mount('#app')
