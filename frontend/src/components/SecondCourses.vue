<template>

  <div>

    <v-list id="list" class="overflow-y-auto" height="250px">
      Select a {{ bucketNumber }} course

      <v-divider></v-divider>

      <!-- LIST OF POSSIBLE SECOND COURSES -->
      <v-list-group color="#c65353" v-for="(course, i) in path.priority2" :key="i">

        <!-- MAKES THE COURSE EXPANDABLE -->
        <template v-slot:activator>
          <v-list-item-content>
            <v-list-item-title>{{ findCourse(course).fields.name }}</v-list-item-title>
          </v-list-item-content>
        </template>

        <v-list-item>

          <!-- COURSE DESCRIPTION AND BUTTON TO SELECT -->
          <v-card flat class="mt-2 mb-2" color="#dcdcdc" width="100%">
            <v-card-text>{{findCourse(course).fields.description}}</v-card-text>

            <v-card-actions>
              <v-spacer></v-spacer>
              <v-btn depressed @click="selectCourse(findCourse(course))" class="mr-2 mb-2 text-capitalize">
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
      bucketNumber: 'second',
      nextBucketNumber: 'third',
      allCourses: cJson
    }
  },
  methods: {
    ...mapMutations(['setSelectedCourse2']),
    selectCourse(course) {
      this.setSelectedCourse2(course.fields.name);
      console.log(course)
      this.$emit('nextBucket', this.nextBucketNumber)
      this.$root.$emit('makeThirdCourseEditable', true)
      this.$root.$emit('changeCurrent', 3)
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
