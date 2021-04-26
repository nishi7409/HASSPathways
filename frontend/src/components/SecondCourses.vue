<template>

  <div>

    <v-list id="list" class="overflow-y-auto" height="250px">
      Select a {{ bucketNumber }} course

      <v-divider></v-divider>

      <!-- LIST OF POSSIBLE SECOND COURSES -->
      <v-list-group color="#c65353" v-for="(course, i) in findAllCourses(path)" :key="i">
        <!-- MAKES THE COURSE EXPANDABLE -->
        <template v-slot:activator>
          <v-list-item-content>
            <v-list-item-title>{{ course.fields.prefix +" "+course.fields.ID+" – "+course.fields.name +" "}}
            <v-chip v-if="course.fields.major_restrictive" medium color="red" class="mr-2" text-color="white">Major Restricted</v-chip>
            <v-chip v-if="course.fields.CI" style="float:right"  medium color="black" class="mr-2" text-color="white">Communication Intensive</v-chip>
            <v-chip v-if="course.fields.HI" style="float:right" medium color="#87AEE8" class="mr-2" text-color="#000000">HASS Inquiry</v-chip>
            <v-chip v-if="course.fields.DI" style="float:right" medium color="#ff63bc" class="mr-2" text-color="black">Data Intensive</v-chip>
            <v-chip v-if="course.fields.fall" style="float:right" medium color="#ff8247" class="mr-2" text-color="black">Fall</v-chip>
            <v-chip v-if="course.fields.spring" style="float:right" medium color="#54ff7c" class="mr-2" text-color="black">Spring</v-chip>
            <v-chip v-if="course.fields.summer" style="float:right" medium color="#ffeb54" class="mr-2" text-color="black">Summer</v-chip>
            </v-list-item-title>
          </v-list-item-content>
        </template>

        <v-list-item>

          <!-- COURSE DESCRIPTION AND BUTTON TO SELECT -->
          <v-card flat class="mt-2 mb-2" color="#dcdcdc" width="100%">
            <v-card-text>{{course.fields.description}}</v-card-text>

            <v-card-actions>
              <v-spacer></v-spacer>
              <v-btn depressed @click="selectCourse(course)" class="mr-2 mb-2 text-capitalize">
                <span>
                  <i style="color: #c65353" class="fas fa-plus"></i>
                  Add Course
                </span>
              </v-btn>
            </v-card-actions>
          </v-card>
        </v-list-item>

      </v-list-group>
    </v-list>

  </div>
  
</template>

<script>

import { mapGetters, mapMutations } from 'vuex'
import cJson from '../../../JSONfiles/courses.json'


export default {
  props: ['path'],
  data() {
    return {
      currentCourse: "",
      bucketNumber: 'second',
      nextBucketNumber: 'third',
      allCourses: cJson
    }
  },
  methods: {
    ...mapGetters(['firstCourse','secondCourse']),
    ...mapMutations(['setSelectedCourse2', 'setSelectedCourse3']),
    findAllCourses(path){
      var courses = []
      for (var x = 0; x<path.priority2.length; x++){
        courses.push(this.findCourse(path.priority2[x]))
      }
      return courses
    },
    selectCourse(course) {
      if (course.fields.name == this.firstCourse().fields.name){
        this.$toast.clear()
        this.$toast.error("Can't choose a course you've already chosen!", {
          position: "top-right",
          timeout: 3000,
          pauseOnFocusLoss: true,
          hideProgressBar: true,
          rtl: false,
          closeButton: "button",
        });
      }else{
        this.setSelectedCourse2(course);
        if (this.$store.editingCourses){
          this.setSelectedCourse3(null);
        }
        console.log(course)
        this.$emit('nextBucket', this.nextBucketNumber)
        this.$root.$emit('makeThirdCourseEditable', true)
        this.$root.$emit('changeCurrent', 3)
        this.$root.$emit(`closePanels`)
      }
    },
    findCourse(course){
      var courses = this.allCourses
      for (var courseKey in courses){
        if (course == courses[courseKey].pk){
          this.currentCourse = courses[courseKey];
          return courses[courseKey]
        }
      }
    }
  }
}
</script>

<style scoped>

</style>
