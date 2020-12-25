<template>

  <div>

    <v-container fluid class="mt-4" v-if="getOptions.length > 0">
      <div id="buttonAndNav_holder">
        <div id="clearButtons" class="ml-4">
          <v-btn @click="removePathway(i)" color="#c65353" depressed class="white--text text-capitalize mr-2">Delete Pathway</v-btn>
          <v-btn @click="clearActivity()" color="#c65353" depressed class="white--text text-capitalize">Clear All Pathways</v-btn>
        </div>
        <div id="pathwaysNavigation" class="mr-4">
          <div v-if="getOptions.length > 0">
            <i @click="goToLastPathway()" class="fa fa-caret-left pointer"></i>
            <span class="mr-2 ml-2">{{ i + 1 }} / {{ getOptions.length }}</span>
            <i @click="goToNextPathway()" class="fa fa-caret-right pointer"></i>
          </div>
        </div>
      </div>
    </v-container>
    
    <v-container fluid v-if="getOptions.length > 0">
      
      <v-card flat>

        <v-card-title>
          {{ currentCourse.pathway.name }}
        </v-card-title>

        <v-card-subtitle>

          <!-- loop button x times -->
          <v-btn tile depressed shaped x-large width="33.333%" color="pink" dark class="text-trunctate text-capitalize rounded-left" v-on:click="selectCourse(currentCourse.first_course)">
            <v-icon>mdi-numeric-1</v-icon>
            {{ currentCourse.first_course }}
          </v-btn>

          <v-btn tile depressed shaped x-large width="33.333%" color="orange" dark class="text-truncate text-capitalize" @click="selectCourse(currentCourse.second_course)">
            <v-icon>mdi-numeric-2</v-icon>
            {{ currentCourse.second_course }}
          </v-btn>

          <v-btn tile depressed shaped x-large width="33.333%" color="blue" dark class="text-truncate text-capitalize rounded-right" @click="selectCourse(currentCourse.third_course)">
            <v-icon>mdi-numeric-3</v-icon>
            {{ currentCourse.third_course }}
          </v-btn>

        </v-card-subtitle>

        <!-- card information -->
        <v-card-text>
          <v-card width="100%" height="90%" outlined id="rounded-left">
          
            <!-- course name & important chips -->
            <template>
              <v-card-title v-if="specifiedCourse == 'None'">
                {{ currentCourse.first_course }}
              </v-card-title>

              <v-card-title v-else>
                {{ this.specifiedCourse }}
              </v-card-title>
            </template>

            <v-card-subtitle>
              <v-chip small color="orange" class="mr-2 mt-2" text-color="white">IHSS 1140</v-chip>
              <v-chip small color="red" class="mr-2 mt-2" text-color="white">Required</v-chip>
              <v-chip small color="green" class="mr-2 mt-2" text-color="white">Major Restricted</v-chip>
              <v-chip small color="green" class="mr-2 mt-2" text-color="white">Gateway Course</v-chip>
              <v-chip small color="red" class="mr-2 mt-2" text-color="white">HASS Inquiry</v-chip>
            </v-card-subtitle>

            <v-divider></v-divider>

            <template>
              <!-- course description -->
              <v-card-text class="font-weight-black" v-if="specifiedCourse == 'None'">
                {{ currentCourse.first_course }}'s course description IF specifiedCourse EQUALS NONE
              </v-card-text>

              <v-card-text class="font-weight-black" v-else>
                {{ this.specifiedCourse }}'s course description IF specifiedCourse DOESN'T EQUAL NONE
              </v-card-text>
            </template>

          </v-card>
        </v-card-text>

      </v-card>

    </v-container>

    <v-container v-else>
      <center>
        <v-btn depressed class="text-capitalize mt-4 mb-4" :to="{name: 'home'}">Explore pathways</v-btn>
      </center>

      <v-card flat>

        <v-card-subtitle>

        <!-- loop button x times -->
        <v-skeleton-loader type="heading"></v-skeleton-loader>

        </v-card-subtitle>

        <!-- card information -->
        <v-card-text>
          <v-card width="100%" height="90%" outlined id="rounded-left">
          
            <!-- course name & important chips -->
            <v-skeleton-loader class="mr-2 mt-2" type="card-heading"></v-skeleton-loader>

            <v-divider></v-divider>

            <template>
              <!-- course description -->
              <v-skeleton-loader width="100%" class="mr-2 mt-2" type="text@3"></v-skeleton-loader>
            </template>

          </v-card>
        </v-card-text>

      </v-card>

    </v-container>

  </div>
  
</template>

<script>

import { mapGetters, mapMutations } from 'vuex'

export default {
  props: ['path'],
  data() {
    return {
      specifiedCourse: "None",
      i: 0
    }
  },
  methods: {
    ...mapMutations(['clear', 'removePath']),
    selectCourse(course) {
      this.specifiedCourse = course;
    },
    goToNextPathway() {
      if (this.i == this.getOptions.length - 1) {
        this.i = 0
      } else if (this.i < this.getOptions.length - 1) {
        this.i++
      }
    },
    goToLastPathway() {
      if (this.i == 0) {
        this.i = this.getOptions.length - 1
      } else if (this.i > 0) {
        this.i--
      }
    },
    clearActivity() {
      console.log("clearing")
      this.clear()
    },
    removePathway(i) {
      console.log("remove " + i)
      this.removePath(i)

      console.log("i " + i)
      if (i == this.getOptions.length) {
        this.i -= 1
      }
    }
  },
  computed: {
    ...mapGetters(['getOptions', 'getOptionsLength', 'pathway']),
    optionsLength() {
      return this.$store.getters.getOptionsLength;
    },
    storedCoursesAppender() {
      var storedCourses = []

      // if no options (no activity)
      console.log("options " + this.getOptions.length)
      if (this.$store.getters.getOptions.length === 0) return storedCourses;

      var array_length, innerLoop;
      for (array_length = 0; array_length < this.$store.getters.getOptions.length; array_length++){
        var firstCourse, secondCourse, thirdCourse;
        for (innerLoop = 1; innerLoop < this.$store.getters.getOptions[array_length].length; innerLoop++){
          if (innerLoop === 1) firstCourse = this.$store.getters.getOptions[array_length][innerLoop];
          if (innerLoop === 2) secondCourse = this.$store.getters.getOptions[array_length][innerLoop]
          if (innerLoop === 3) thirdCourse = this.$store.getters.getOptions[array_length][innerLoop];
        }
        var path = this.$store.getters.getOptions[array_length][0]
        var object = {pathway: path, first_course: firstCourse, second_course: secondCourse, third_course: thirdCourse}
        storedCourses.push(object);
      }

      console.log(storedCourses)
      return storedCourses;
    },
    currentCourse() {
      if (this.optionsLength > 0) {
        return this.storedCoursesAppender[this.i]
      }
      return ""
    }
  }
}

</script>

<style scoped>

#buttonAndNav_holder {
  overflow: hidden;
}

#clearButtons {
  float: left;
}

#pathwaysNavigation {
  float: right;
}

.pointer {
  cursor: pointer;
}

.rounded-left {
  border-radius: 5px 0px 0px 5px;
}

.rounded-right {
  border-radius: 0px 5px 5px 0px;
}

</style>
