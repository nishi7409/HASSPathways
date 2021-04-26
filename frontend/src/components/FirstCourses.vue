<template>

  <div>

    <v-list id="list" class="overflow-y-auto" height="250px">
      Select a {{ bucketNumber }} course

      <v-divider></v-divider>

      <!-- LIST OF POSSIBLE FIRST COURSES -->
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
            <v-card-text>{{ course.fields.description }}</v-card-text>

            <v-card-actions>
              <v-spacer></v-spacer>
              <v-btn depressed @click="selectCourse(course,path)" class="mr-2 mb-2 text-capitalize">
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

import { mapMutations } from 'vuex'
import cJson from '../../../JSONfiles/courses.json'

export default {
  props: ['path'],
  data() {
    return {
      category: '',
      bucketNumber: 'first',
      nextBucketNumber: 'second',
      allCourses: cJson
    }
  },
  methods: {
    ...mapMutations(['setSelectedCourse1', 'setSelectedCourse2', 'setSelectedCourse3', 'setSelectedPathway']),
    findAllCourses(path){
      var courses = []
      for (var x = 0; x<path.priority1.length; x++){
        courses.push(this.findCourse(path.priority1[x]))
      }
      return courses
    },
    selectCourse(course, path) {
      this.setSelectedPathway(path.pathName)
      this.setSelectedCourse1(course);
      if (this.$store.editingCourses){
        this.setSelectedCourse2(null);
        this.setSelectedCourse3(null);
      }
      console.log(course)
      this.$emit('nextBucket', this.nextBucketNumber)
      this.$root.$emit('makeSecondCourseEditable', true)
      this.$root.$emit('changeCurrent', 2)
      this.$root.$emit(`closePanels`)
    },
    findCourse(course){
      var courses = this.allCourses
      for (var courseKey in courses){
        if (course == courses[courseKey].pk){
          return courses[courseKey]
        }
      }
    }
  }
}
</script>

<style scoped>

</style>
