<template>

    <div class="progress">
      <div>
        <v-card flat class="pl-3 pt-5 pb-1 text-middle" v-if= "this.$store.editingCourses == true"> <!--  v-if= "courseEditStatus == true" -->
          <span class= "pt-3 headline font-weight-bold">Editing Pathway </span>
        </v-card>
      </div>

      <div id="stepper">

        <v-stepper id="progress" class="elevation-0" :value="current">

          <v-stepper-header class="elevation-0">

            <v-btn @click="clearProgress()" color="#c65353" depressed class="white--text text-capitalize button ml-2 mr-2">Clear</v-btn>

            <v-stepper-step :step="1" :complete="numberOfCoursesSelected > 0" @click="goToCourse(1)" :editable='firstCourseEditable' edit-icon="done" v-if= "this.current != 1" color="#c65353">
            {{coursesList.firstCourse}} <!-- Normal view -->
            </v-stepper-step>

            <v-stepper-step :step="1" :complete="numberOfCoursesSelected > 0" @click="goToCourse(1)" :editable='firstCourseEditable' edit-icon="create" v-if= "this.current == 1" color="#919191">
            {{coursesList.firstCourse}} <!-- Selected view -->
            </v-stepper-step>

            <v-divider></v-divider>

            <v-stepper-step :step="2" :complete="numberOfCoursesSelected > 1" @click="goToCourse(2)" :editable='secondCourseEditable' edit-icon="done" v-if= "this.current != 2" color="#c65353">
            {{coursesList.secondCourse}} <!-- Normal view -->
            </v-stepper-step>

            <v-stepper-step :step="2" :complete="numberOfCoursesSelected > 1" @click="goToCourse(2)" :editable='secondCourseEditable' edit-icon="create" v-if= "this.current == 2" color="#919191">
            {{coursesList.secondCourse}} <!-- Selected view -->
            </v-stepper-step>

            <v-divider></v-divider>

            <v-stepper-step :step="3" :complete="numberOfCoursesSelected > 2" @click="goToCourse(3)" :editable='thirdCourseEditable' edit-icon="done" v-if= "this.current != 3" color="#c65353">
            {{coursesList.thirdCourse}} <!-- Normal view -->
            </v-stepper-step>

            <v-stepper-step :step="3" :complete="numberOfCoursesSelected > 2" @click="goToCourse(3)" :editable='thirdCourseEditable' edit-icon="create" v-if= "this.current == 3" color="#919191">
            {{coursesList.thirdCourse}} <!-- Selected view -->
            </v-stepper-step>

          </v-stepper-header>

        </v-stepper>
      </div>
    </div>

</template>

<script>

import { mapMutations, mapGetters } from 'vuex'

export default {
  data(){
    return {
      courseNumber: "",
      firstCourseEditable: true,
      secondCourseEditable: false,
      thirdCourseEditable: false,
      current: 1
    }
  },
  methods: {
    ...mapMutations(['setSelectedCourse1', 'setSelectedCourse2', 'setSelectedCourse3', 'incrementCount', 'goToCourse']),
    clearProgress() {
      console.log("clear progress")
      this.setSelectedCourse1(null)
      this.setSelectedCourse2(null)
      this.setSelectedCourse3(null)
      // this.incrementCount()
      this.$root.$emit('changeWhichCourse', "first")
      this.$root.$emit('changeCurrent', 1)
      this.$root.$emit('makeSecondCourseEditable', false)
      this.$root.$emit('makeThirdCourseEditable', false)
    },
    goToCourse(num) {
      if (num == 1) {
        this.courseNumber = "first"
        this.$root.$emit('changeWhichCourse', "first")
        if (this.firstCourseEditable)
          this.$emit('nextBucket', 1)
        this.current = 1
      } else if (num == 2) {
        if (this.firstCourse != null) {
          this.courseNumber = "second"
          this.$root.$emit('changeWhichCourse', "second")
          if (this.secondCourseEditable)
            this.$emit('nextBucket', 2)
          this.current = 2
        }
      } else if (num == 3) {
        if (this.secondCourse != null) {
          this.courseNumber = "third"
          this.$root.$emit('changeWhichCourse', "third")
          if (this.thirdCourseEditable)
            this.$emit('nextBucket', 3)
          this.current = 3
        }
      }
    }
  },
  // we use a computed property to automatically update the 
  // number of steps shown as complete on the progressbar based on the 
  // current application state
  computed: {
    ...mapGetters(['progressBarStatus', 'firstCourse', 'secondCourse', 'thirdCourse']),
    numberOfCoursesSelected () {
      return this.progressBarStatus;
    },
    coursesList() {
      return {
        firstCourse: this.firstCourse ? this.firstCourse.fields.name : "No Course Selected",
        secondCourse: this.secondCourse ? this.secondCourse.fields.name : "No Course Selected",
        thirdCourse: this.thirdCourse ? this.thirdCourse.fields.name : "No Course Selected"
      }
    },
    secondEditable() {
      if (this.firstCourse) {
        return true
      }
      return false
    },
    thirdEditable() {
      if (this.secondCourse) {
        return true
      }
      return false
    },
    activeStep() {
      if (this.firstCourse != null) {
        if (this.secondCourse != null) {
          if (this.thirdCourse != null) {
            return 3
          }
          return 3
        }
        return 2
      }
      return 1
    }
  },
  mounted() {
    this.$root.$on('editAtFirstCourse', () => {
      this.goToCourse(1);
    }),
    this.$root.$on('resetProgress', () => {
      this.clearProgress()
    }),
    this.$root.$on('changeWhichCourse', (course) => {
      this.courseNumber = course
    }),
    this.$root.$on('makeFirstCourseEditable', (editable) => {
      this.firstCourseEditable = editable
    }),
    this.$root.$on('makeSecondCourseEditable', (editable) => {
      this.secondCourseEditable = editable
    }),
    this.$root.$on('makeThirdCourseEditable', (editable) => {
      this.thirdCourseEditable = editable
    }),
    this.$root.$on('changeCurrent', (current) => {
      this.current = current
    })
    this.secondCourseEditable = this.secondEditable,
    this.thirdCourseEditable = this.thirdEditable,
    this.current = this.activeStep
  }
}

</script>

<style>

  .theme--light.v-stepper .v-stepper__step--editable:hover {
    background: rgba(198, 83, 83, 0.2);
  }

  .button {
    margin: auto;
  }

  .progress {
    position: fixed;
    z-index: 100;
    width: 100%;
  }

  #progress {
    border-radius: 0;
  }

</style>