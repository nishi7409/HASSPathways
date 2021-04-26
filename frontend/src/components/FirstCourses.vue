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
            <v-chip v-if="course.fields.HI" style="float:right"  small color="green"  text-color="black">Hass Inquiry</v-chip>
            <p class="pa-1" style="float:right"></p>
            <v-chip v-if="course.fields.CI" style="float:right" small color="green"  text-color="black">Comm Intensive</v-chip>
            <p class="pa-1" style="float:right"></p>
            <v-chip v-if="course.fields.DI" style="float:right" small color="green"  text-color="black">DI</v-chip>
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
import cJson from './courses.json'

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
    ...mapMutations(['setSelectedCourse1','setSelectedPathway']),
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
