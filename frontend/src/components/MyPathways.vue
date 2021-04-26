<template>

  <div>

    <v-container fluid class="mt-4" v-if="getOptions.length > 0">
      <div id="buttonAndNav_holder">
        <div id="clearButtons">
          <v-btn @click="removePathway(i)" color="#c65353" depressed class="white--text text-capitalize mr-2">Delete This Pathway</v-btn>
          <v-btn @click="clearActivity()" color="#c65353" depressed class="white--text text-capitalize mr-2">Clear All Pathways</v-btn>
          <v-btn @click="makeCoursesEditable()" color="#c65353" depressed class="white--text text-capitalize">Edit Pathway</v-btn>
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
    
    <v-container fluid v-if="getOptions.length == 0"> 
      <!-- If no Pathways have been specified yet -->
      <!-- If this isnt coded, then the 'My Pathways' page will show a loading animation forever if no pathways stored -->

      <v-container fill-height>
          <v-row justify="center" align="center" class= "pt-10">
              <v-col sm="4" class= "font-weight-regular pt-10 pa-8">
                  <p class= "headline" > This place seems pretty lonely. </p>

                  <span class = "headline"> You can add Pathways from the </span>
                  <span class= "headline font-weight-black">Add Pathways </span>
                  <span class= "headline">section.</span>
              </v-col>
          </v-row>
      </v-container>
    </v-container>


    <v-container fluid v-if="getOptions.length > 0">  <!-- If at least one Pathway has been Created -->

        <!-- Pathway Name Indicator -->
        <div>
          <span class= "font-weight-bold"> 
            Pathway
          </span>
          <p class="headline font-weight-black"> 
            {{ currentCourse.pathway }}
          </p>
        </div>

      <!-- Expansion Pannel Setup Housing All 3 Expansion Panels -->
      <v-card>
        <v-expansion-panels flat outlined dark tile accordion hover multiple class="expansion-panel overflow-y-auto">

          <!-- COURSE 1 EXPANSION PANEL -->
          <v-expansion-panel>  
            <v-expansion-panel-header color="#c65353" id="expansion-header" class= "font-weight-black pa-8">
              {{ currentCourse.first_course.fields.prefix +" "+currentCourse.first_course.fields.ID+" – "+currentCourse.first_course.fields.name   }}

              <template v-slot:actions>
                <v-icon color="white">$expand</v-icon>
              </template>
            </v-expansion-panel-header>

            <v-expansion-panel-content color= "white">
              <v-card-subtitle class= "pb-0 pl-1">
                <v-chip v-if="currentCourse.first_course.fields.major_restrictive" medium color="red" class="mr-2 mt-2" text-color="white">Major Restricted</v-chip>
                <v-chip v-if="currentCourse.first_course.fields.CI" medium color="black" class="mr-2 mt-2" text-color="white">Communication Intensive</v-chip>
                <v-chip v-if="currentCourse.first_course.fields.HI" medium color="#87AEE8" class="mr-2 mt-2" text-color="black">HASS Inquiry</v-chip>
                <v-chip v-if="currentCourse.first_course.fields.DI" medium color="#ff63bc" class="mr-2 mt-2" text-color="black">Data Intensive</v-chip>
                <v-chip v-if="currentCourse.first_course.fields.fall" medium color="#ff8247" class="mr-2 mt-2" text-color="black">Fall</v-chip>
                <v-chip v-if="currentCourse.first_course.fields.spring" medium color="#54ff7c" class="mr-2 mt-2" text-color="black">Spring</v-chip>
                <v-chip v-if="currentCourse.first_course.fields.summer" medium color="#ffeb54" class="mr-2 mt-2" text-color="black">Summer</v-chip>
              </v-card-subtitle>

              <!-- COURSE 1 DESCRIPTION -->
              <v-card flat color="#c65353" class= "mt-1" >
                <v-card-text class= "mt-6 white--text font-weight-black">
                  <p> {{currentCourse.first_course.fields.description }} </p>
                </v-card-text>
              </v-card>
            </v-expansion-panel-content>
          </v-expansion-panel>

          <!-- COURSE 2 EXPANSION PANEL -->
          <v-expansion-panel class="mt-3">  
            <v-expansion-panel-header color="#c65353" id="expansion-header"  class= "font-weight-black pa-8">
            {{ currentCourse.second_course.fields.prefix +" "+currentCourse.second_course.fields.ID+" – "+currentCourse.second_course.fields.name   }}

              <template v-slot:actions>
                <v-icon color="white">$expand</v-icon>
              </template>
            </v-expansion-panel-header>

            <v-expansion-panel-content color= "white">
              <v-card-subtitle class= "pb-0 pl-1">
                <v-chip v-if="currentCourse.second_course.fields.major_restrictive" medium color="red" class="mr-2 mt-2" text-color="white">Major Restricted</v-chip>
                <v-chip v-if="currentCourse.second_course.fields.CI" medium color="black" class="mr-2 mt-2" text-color="white">Communication Intensive</v-chip>
                <v-chip v-if="currentCourse.second_course.fields.HI" medium color="#87AEE8" class="mr-2 mt-2" text-color="black">HASS Inquiry</v-chip>
                <v-chip v-if="currentCourse.second_course.fields.DI" medium color="#ff63bc" class="mr-2 mt-2" text-color="black">Data Intensive</v-chip>
                <v-chip v-if="currentCourse.second_course.fields.fall" medium color="#ff8247" class="mr-2 mt-2" text-color="black">Fall</v-chip>
                <v-chip v-if="currentCourse.second_course.fields.spring" medium color="#54ff7c" class="mr-2 mt-2" text-color="black">Spring</v-chip>
                <v-chip v-if="currentCourse.second_course.fields.summer" medium color="#ffeb54" class="mr-2 mt-2" text-color="black">Summer</v-chip>
              </v-card-subtitle>

              <!-- COURSE 2 DESCRIPTION -->
              <v-card flat color="#c65353" class= "mt-1">
                <v-card-text class="mt-6 white--text font-weight-black">
                  <p> {{currentCourse.second_course.fields.description}} </p>
                </v-card-text>
              </v-card>
            </v-expansion-panel-content>
          </v-expansion-panel>
          
          <!-- COURSE 3 EXPANSION PANEL -->
          <v-expansion-panel class="mt-3">  
            <v-expansion-panel-header color="#c65353" id="expansion-header" class= "font-weight-black pa-8">
              {{ currentCourse.third_course.fields.prefix +" "+currentCourse.third_course.fields.ID+" – "+currentCourse.third_course.fields.name   }}

              <template v-slot:actions>
                <v-icon color="white">$expand</v-icon>
              </template>
            </v-expansion-panel-header>

            <v-expansion-panel-content color= "white">
              <v-card-subtitle class= "pb-0 pl-1">
                <v-chip v-if="currentCourse.third_course.fields.major_restrictive" medium color="red" class="mr-2 mt-2" text-color="white">Major Restricted</v-chip>
                <v-chip v-if="currentCourse.third_course.fields.CI" medium color="black" class="mr-2 mt-2" text-color="white">Communication Intensive</v-chip>
                <v-chip v-if="currentCourse.third_course.fields.HI" medium color="#87AEE8" class="mr-2 mt-2" text-color="black">HASS Inquiry</v-chip>
                <v-chip v-if="currentCourse.third_course.fields.DI" medium color="#ff63bc" class="mr-2 mt-2" text-color="black">Data Intensive</v-chip>
                <v-chip v-if="currentCourse.third_course.fields.fall" medium color="#ff8247" class="mr-2 mt-2" text-color="black">Fall</v-chip>
                <v-chip v-if="currentCourse.third_course.fields.spring" medium color="#54ff7c" class="mr-2 mt-2" text-color="black">Spring</v-chip>
                <v-chip v-if="currentCourse.third_course.fields.summer" medium color="#ffeb54" class="mr-2 mt-2" text-color="black">Summer</v-chip>
                
              </v-card-subtitle>

              <!-- COURSE 3 DESCRIPTION -->
              <v-card flat color="#c65353" class= "mt-1">
                <v-card-text class="mt-6 white--text font-weight-black">
                  <p> {{currentCourse.third_course.fields.description}}</p>
                </v-card-text>
              </v-card>
            </v-expansion-panel-content>
          </v-expansion-panel>
        </v-expansion-panels>
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
    ...mapMutations(['setSelectedPathway','setSelectedCourse1', 'setSelectedCourse2', 'setSelectedCourse3', 'clear', 'removePath']),
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
    },
    makeCoursesEditable() {
      this.$root.$emit('editAtFirstCourse')
      this.$store.editingCourses = true
      this.$store.targetEditIndex = this.i
      this.$root.$emit('makeFirstCourseEditable', true)
      this.$root.$emit('makeSecondCourseEditable', true)
      this.$root.$emit('makeThirdCourseEditable', true)
      this.setSelectedPathway(this.getOptions[this.i][0])
      this.setSelectedCourse1(this.getOptions[this.i][1])
      this.setSelectedCourse2(this.getOptions[this.i][2])
      this.setSelectedCourse3(this.getOptions[this.i][3])
      this.$toast.clear()
      this.$toast.info("Press the save button in the lower\nright to finish editing your pathway.", {
        color: "#4FDEF5",
        position: "top-right",
        timeout: 4000,
        pauseOnFocusLoss: true,
        hideProgressBar: true,
        rtl: false,
        closeButton: "button",
      });
      this.$router.push('home');
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
        for (innerLoop = 0; innerLoop < this.$store.getters.getOptions[array_length].length; innerLoop++){
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

.element {
  position: relative;
  top: 50%;
  -webkit-transform: translateY(-50%);
  -ms-transform: translateY(-50%);
  transform: translateY(-50%);
}

.v-text-field {
    font-size: 5em;
  }

</style>
