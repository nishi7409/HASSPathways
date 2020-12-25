<template>

  <div>

    <v-list id="list" class="overflow-y-auto" height="250px">
      Select a {{ bucketNumber }} course

      <v-divider></v-divider>

      <!-- LIST OF POSSIBLE FIRST COURSES -->
      <v-list-group color="#c65353" v-for="(course, i) in path.Courses" :key="i">

        <!-- MAKES THE COURSE EXPANDABLE -->
        <template v-slot:activator>
          <v-list-item-content>
            <v-list-item-title>{{ course }}</v-list-item-title>
          </v-list-item-content>
        </template>

        <v-list-item>

          <!-- COURSE DESCRIPTION AND BUTTON TO SELECT -->
          <v-card flat class="mt-2 mb-2" color="#dcdcdc" width="100%">
            <v-card-text>Description of course here</v-card-text>

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

import { mapMutations } from 'vuex'

export default {
  props: ['path'],
  data() {
    return {
      bucketNumber: 'first',
      nextBucketNumber: 'second'
    }
  },
  methods: {
    ...mapMutations(['setSelectedCourse1']),
    selectCourse(course) {
      this.setSelectedCourse1(course);
      console.log(course)
      this.$emit('nextBucket', this.nextBucketNumber)
      this.$root.$emit('makeSecondCourseEditable', true)
      this.$root.$emit('changeCurrent', 2)
    }
  }
}
</script>

<style scoped>

</style>
