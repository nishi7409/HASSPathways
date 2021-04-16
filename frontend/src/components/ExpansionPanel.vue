

<template>
  <div>
    <ProgressBar/>
    
    <v-expansion-panels v-model="panel" flat outlined tile accordion hover multiple class="expansion-panel overflow-y-auto">
      <v-expansion-panel @click="selectPathway(path)" v-for="(path, i) in filteredPathways" :key="i">
        
        <v-expansion-panel-header color="#c65353" id="expansion-header">
          {{ path.name }}
          <template v-slot:actions>
            <v-icon color="white">$expand</v-icon>
          </template>
        </v-expansion-panel-header>

        <v-expansion-panel-content>
          <v-card flat color="#dcdcdc">
            <v-card-text class="mt-4">{{ path.pathDescription }}</v-card-text>
          </v-card>

          <FirstCourses @nextBucket="moveToNextBucket" v-if="courseNumber=='first'" :path="path"/>
          <SecondCourses @nextBucket="moveToNextBucket" v-else-if="courseNumber=='second'" :path="path"/>
          <ThirdCourses v-else-if="courseNumber=='third'" :path="path"/>
        </v-expansion-panel-content>

        <v-divider color="white"></v-divider>

      </v-expansion-panel>
      
    </v-expansion-panels>
  <div>
    <v-btn large fixed bottom right fab id = "button1" v-if="courseNumber=='third' || this.$store.editingCourses == true" @click="savePathway()" class="stickyButton">
      <v-icon style="color: white">
          mdi-content-save
      </v-icon>
    </v-btn>
    </div>
  </div>
</template>

<script>

import ProgressBar from './ProgressBar.vue'
import FirstCourses from './FirstCourses'
import SecondCourses from './SecondCourses'
import ThirdCourses from './ThirdCourses'
import { mapGetters, mapMutations } from 'vuex'

export default {
  components: {
    FirstCourses,
    SecondCourses,
    ThirdCourses,
    ProgressBar,
  },
  data() {
    return {
      pathways: [
        { name: 'Artificial Intelligence', pathDescription: "Artificial Intelligence is quickly becoming pervasive in our lives. Study how Artificial Intelligence can benefit from concepts and ideas from cognitive science, and explore the ways in which Artificial Intelligence is changing our lives.", Courses: ["Minds and Machines", "AI and Society", "Are Humans Rational?"], secondCourses: ["Introduction to Cognitive Science"], thirdCourses: ["Cognitive Modeling, Programming for Cognitive Science and AI", "Game AI", "Intelligent Virtual Agents", "Language Endowed Intelligent Agents", "Learning and Advanced Game AI"] },
        { name: 'Chinese Language', pathDescription: "Integrated with Chinese culture, students will learn all four types of language skills (listening, speaking, reading, and writing). After completing the Chinese pathway, students will be able to communicate in Chinese at their targeted proficiency levels and think critically and creatively with global and multicultural awareness.", Courses: ["AI and Society", "2", "3", "4"], secondCourses: ["Introduction to Cognitive Science"] },
        { name: 'History', pathDescription: "The pathway in History is designed for students interested in US and world history. Courses primarily focus on the social history and evolution of technology, scientific enterprise, medicine, and law.", Courses: ["AI and Society", "2", "3", "4"], secondCourses: ["1"] },
        { name: 'Creative Design and Innovation', pathDescription: "This pathway looks at creative design and innovation from various humanities, arts, and social science points of view. Students will learn about the cognitive and communicative principles behind design and innovation, the economic policies, markets, and other social institutions driving and shaping design and innovation, and how to engage in sustainable and socially responsible design and innovation for local and global impact.", Courses: ["1", "2", "3", "4"] },
        { name: 'Arts History, Theory, and Criticism' },
        { name: 'Behavioral and Cognitive Neuroscience' },
        { name: 'Design, Innovation, and Society' },
        { name: 'Economics' },
        { name: 'Economics of Banking & Finance' },
        { name: 'Other' },
        { name: 'Other' },
        { name: 'Other' },
        { name: 'Other' },
        { name: 'Other' },
        { name: 'Other' }
      ],
      courseNumber: 'first',
      savedCourses: [],
      filter: '',
      panel: []
    }
  },
  methods: {
    ...mapGetters(['thirdCourse',`secondCourse`,`firstCourse`]),
    ...mapMutations(['setSelectedPathway','saveButton', 'removePath']),
    pathwayExist(courseCombo){
      for (var i = 0; i < this.$store.getters.getOptions.length; i++) {
        if (this.$store.getters.getOptions[i][1] == courseCombo[0] &&
          this.$store.getters.getOptions[i][2] == courseCombo[1] &&
          this.$store.getters.getOptions[i][3] == courseCombo[2]) {
            console.log("exists")
            return true
        }
      }
      console.log("does not exist")
      return false
    },
    savePathway(){
      console.log(localStorage.getItem('course1'))
      // If the third course has been chosen or not
      if (this.$store.getters.thirdCourse){
        // If the pathway already exists reject save
        if (this.pathwayExist([this.$store.getters.firstCourse, this.$store.getters.secondCourse, this.$store.getters.thirdCourse])) {
          if (this.$store.editingCourses == true){
            this.$store.editingCourses = false
            this.$store.targetEditIndex = -1
          }
          this.$toast.clear()
          this.$toast.error("This pathway already exists!", {
            position: "top-right",
            timeout: 3000,
            pauseOnFocusLoss: true,
            hideProgressBar: true,
            rtl: false,
            closeButton: "button",
          });
          this.$root.$emit('resetProgress')
        }else{
          if (this.$store.editingCourses == true){
            this.removePath(this.$store.targetEditIndex)
            this.$store.editingCourses = false
            this.$store.targetEditIndex = -1
          }
          this.saveButton()
          this.$root.$emit('resetProgress')
          this.$toast.clear()
          this.$toast.success("Saved Pathway!", {
            position: "top-right",
            timeout: 3000,
            pauseOnFocusLoss: true,
            hideProgressBar: true,
            rtl: false,
            closeButton: "button",
          });
        }
      }else{
        this.$toast.clear()
        this.$toast.error("You haven't chosen three courses yet!", {
          position: "top-right",
          timeout: 3000,
          pauseOnFocusLoss: true,
          hideProgressBar: true,
          closeButton: "button",
        });
      }
      this.$root.$emit(`closePanels`)
    },
    selectPathway(path) {
      console.log(path.name)
      this.setSelectedPathway(path)
    },
    moveToNextBucket(course) {
      this.courseNumber = course
      if (this.courseNumber == "first") {
        this.$root.$emit('changeWhichCourse', "first")
      } else if (this.courseNumber == "second") {
        this.$root.$emit('changeWhichCourse', "second")
      } else if (this.courseNumber == "third") {
        this.$root.$emit('changeWhichCourse', "third")
      }
    }
  },
  mounted() {
    this.$root.$on('changeWhichCourse', (course) => {
      this.courseNumber = course
    }),
    this.$root.$on('changedFilter', (input) => {
      this.filter = input
    }),
    this.$root.$on('closePanels', () => {
      this.panel = []
    }),
    this.courseNumber = this.bucketNumber;
  },
  computed: {
    ...mapGetters(['pathway', 'firstCourse', 'secondCourse', 'thirdCourse']),
    filteredPathways() {
      var items = this.pathways
      var result = []

      for (var key in items) {
        var item = items[key]
        var courses = item.Courses
        var secondCourses = item.secondCourses

        if (courses != null) {
          for (var i = 0; i < courses.length; i++) {
            var course = courses[i]          
            if (course == this.filter) {
              result[key] = item
            }
          }
        }

        if (courses != null) {
          for (i = 0; i < courses.length; i++) {
            course = courses[i]
            if (course == this.$store.getters.firstCourse) {
              result[key] = item
            }
          }
        }

        if (secondCourses != null) {
          for (i = 0; i < secondCourses.length; i++) {
            course = secondCourses[i]
            if (course == this.$store.getters.secondCourse) {
              result[key] = item
            }
          }
        }
      }

      if (result.length != 0) {
        return result
      }

      return items
    },
    bucketNumber() {
      if (this.$store.getters.firstCourse != null) {
        if (this.$store.getters.secondCourse != null) {
          if (this.$store.getters.thirdCourse != null) {
            return 'third'
          }
          return 'third'
        }
        return 'second'
      }
      return 'first'
    }
  }
}
</script>

<style scoped>

  #button1 {
    margin-bottom: 36px;
    background-color: rgba(180, 67, 52, 0.87);
  }

  .expansion-panel {
    position: relative;
    top: 72px;
    margin-bottom: 36px;
  }
  
  #progressBarAndSave {
    width: 100%;
  }

  #progressBar {
    width: 90%;
  }

  #expansion-header {
    color: white;
  }

</style>
