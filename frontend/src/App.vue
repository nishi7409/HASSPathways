<template>

  <v-app id="app">

    <!-- HEADER -->
    <v-app-bar class="app-bar" app fixed flat color="#c65353" extension-height="100px">
        
        <v-container fluid>
          <v-layout row>

            <!-- TITLE -->
            <v-flex md1 sm11 xs11>
              <router-link to="">
                <v-img class="pl-6 pr-8 ml-4" @click="clearProgress()" height=60 width=40 :src="require('./assets/logo.png')"></v-img>
              </router-link>
            </v-flex>
            
            
            <!-- BUTTONS -->
            <v-col class="text-right" id="topRightButtons">
                <v-btn class="hidden-sm-and-down text-capitalize" rounded elevation="4" depressed id="button" active-class="v-btn--active toolbar-btn-active blue-grey lighten-3" :to="{name: 'activity'}">My Pathways</v-btn>
                <v-btn class="hidden-sm-and-down mr-2 text-capitalize" @click="clearProgress()" active-class="v-btn--active toolbar-btn-active blue-grey lighten-3" rounded elevation="4" depressed id="button" :to="{name: 'home'}">Add Pathways</v-btn>
            </v-col>

          </v-layout>
        </v-container>

    </v-app-bar>

    <!-- ROUTER VIEW -->
    <v-content>
      <router-view></router-view>
    </v-content>
    
    <!-- FOOTER
    <v-footer app>

      <v-layout column>
        <div>

          We love feedback! Come visit our 
          <a href="https://github.com/nishi7409/HASSPathways/issues" target="_blank" style="text-decoration: none">

            <span style="color: #c65353">
              Github Repository
              <i style="color: #c65353" class="fab fa-github"></i>
            </span>

          </a>

        </div>
      </v-layout>
      
      <v-spacer></v-spacer>

      <div>HASS Pathways &copy; {{ new Date().getFullYear() }}</div>

    </v-footer> -->

  </v-app>

</template>

<script>

export default {
  name: 'App',
  data: () => ({
    deleteClicked: false,
    searchInput: "",
    extension: ""
  }),
  methods: {
    handleInput() {
      this.$root.$emit('changedFilter', this.searchInput)
    },
    clearProgress() {
      this.$root.$emit('resetProgress')
      this.$store.editingCourses = false
      location.reload()
    },
  },
  mounted() {
    console.log(this.$vuetify.breakpoint)
    if (localStorage.getItem('extension') == "true") {
      this.extension = true
    }
  },
  watch: {
    extension(newExtension) {
      localStorage.setItem('extension', newExtension)
    }
  }
};

</script>

<style>

#button {
  float: right;
}

#topRightButtons .v-btn::before{
  background-color: transparent;
}


#header {
  height: 70px;
  background-color: #fa8072;
  color: white;
  font-family: 'Muli', sans-serif;
  font-size: 20px;
}

.v-btn--active .v-btn__content { 
  color: black
}  


#title {
  color: white;
  text-decoration: none;
}

#app {
  font-family: 'Muli', sans-serif;
}

#list {
  height: 200px;
}

.combo-box {
  z-index: 200;
}

</style>
