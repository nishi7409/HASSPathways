<template>

  <v-app id="app">

    <!-- HEADER -->
    <v-app-bar class="app-bar" app fixed flat color="#c65353" extension-height="100px">
        
        <v-container fluid>
          <v-layout row>

            <!-- TITLE -->
            <v-flex md1 sm11 xs11>
              <router-link to="/home">
                <v-img class="pl-6 pr-8 ml-4" height=60 width=40 :src="require('./assets/logo.png')"></v-img>
              </router-link>
            </v-flex>

            <v-spacer></v-spacer>
            
            <!-- MENU BAR -->
            <v-icon @click="extension=!extension" class="hidden-md-and-up mt-2" color="white">fa-bars</v-icon>
            
            <!-- BUTTONS -->
            <v-col class="text-right" id="topRightButtons">
                <v-btn class="hidden-sm-and-down text-capitalize" rounded elevation="4" depressed id="button" :to="{name: 'activity'}">My Pathways</v-btn>
                <v-btn class="hidden-sm-and-down mr-2 text-capitalize" 
                  @click="clearProgress()"
                  active-class="v-btn--active toolbar-btn-active"
                  rounded
                  elevation="4"
                  depressed id="button" :to="{name: 'home'}">Add Pathways
                </v-btn>
            </v-col>

<!-- <v-flex md4 id="topRightButtons">
              <v-btn class="hidden-sm-and-down text-capitalize" rounded elevation="4" depressed id="button" :to="{name: 'activity'}">My Pathways</v-btn>
              <v-btn class="hidden-sm-and-down mr-2 text-capitalize" rounded elevation="4" depressed id="button" :to="{name: 'home'}">Add Pathways</v-btn>
            </v-flex> -->

          </v-layout>
        </v-container>

        <!-- HEADER EXTENSION -->
        <template v-if="(this.$vuetify.breakpoint.xs==true || this.$vuetify.breakpoint.sm==true) && extension==true" v-slot:extension>
          <v-layout column>
            
            <v-spacer></v-spacer>

            <!-- BUTTONS -->
            <div class="mb-2">
              <v-btn class="mr-2 text-capitalize" depressed color='primary' :to="{name: 'activity'}">My Pathways</v-btn>
              <v-btn class="text-capitalize" depressed :to="{name: 'home'}">Add Pathways</v-btn>
            </div>
            
          </v-layout>
        </template>
        
    </v-app-bar>

    <!-- ROUTER VIEW -->
    <v-content>
      <router-view></router-view>
    </v-content>

    <!-- FOOTER -->
    <v-footer app>

      <v-layout column>
        <div>

          We love feedback!
          <a href="https://github.com/nishi7409/HASSPathways/issues" target="_blank" style="text-decoration: none">

            <span style="color: #c65353">
              Github Repo
              <i style="color: #c65353" class="fab fa-github"></i>
            </span>

          </a>

        </div>
      </v-layout>
      
      <v-spacer></v-spacer>

      <div>HASS Pathways &copy; {{ new Date().getFullYear() }}</div>

    </v-footer>

  </v-app>

</template>

<script>
import { mapMutations } from 'vuex'

export default {
  name: 'App',
  data: () => ({
    deleteClicked: false,
    items: ['Minds and Machines', 'AI and Society', 'Are Humans Rational?', 'Chinese 1', 'Chinese 2', 'Chinese 3', 'Chinese 4', 'etc'],
    searchInput: "",
    extension: ""
  }),
  methods: {
    handleInput() {
      this.$root.$emit('changedFilter', this.searchInput)
    },
    ...mapMutations(['clearProgress','setSelectedCourse2','setSelectedCourse1']),
    clearProgress() {
      this.$root.$emit('resetProgress')
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
