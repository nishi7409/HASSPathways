<template>
  <div>
      
    <v-container fill-height>
        <span outlined class="pt-8 headline font-weight-black"> Explore Pathways </span>
          <!-- <v-row justify="center" align="center" class= "pt-10"> -->
        <v-row class= "pt-7">
            <v-col cols="6" md="4">

              <v-list light outlined v-if="exploredCourses.length != 0"> 
                <v-list-item v-for="(course, index) in exploredCourses" :key="`course-${index}`">
                  <v-list-item-content>
                    <v-list-item-title>
                      <span class= "pr-3 font-weight-black">
                        ●
                      </span>
                      <span class= "font-weight-black">
                        {{ exploredCourses[index].title }}
                      </span>
                    </v-list-item-title>
                  </v-list-item-content>
                  <v-list-item-icon>
                    <v-btn @click="removeFromExploredCourses(index)" >
                      <v-icon>
                        remove
                      </v-icon>
                    </v-btn>
                  </v-list-item-icon>
                </v-list-item>
              </v-list>

              <v-list light outlined v-if="exploredCourses.length == 0">
                <v-list-item class="ml-15">
                  <span class= "ml-9 font-weight-bold">
                    No courses selected
                  </span>
                </v-list-item>
              </v-list>
            </v-col>

            <v-col cols="12" md="7" class="ml-6">
                <v-card class="pa-2" outlined tile>
                    <v-list>
                      <v-list-group v-for="prefix in prefixes" :key="prefix.title" v-model="prefix.active" :prepend-icon="prefix.action" no-action>
                        <template v-slot:activator>
                          <v-list-item-content>
                            <v-list-item-title v-text="prefix.title" class= "ml-10">
                            </v-list-item-title>
                          </v-list-item-content>
                        </template>

                        <v-list-item v-for="child in prefix.courses" :key="child.title">
                          <v-list-item-content>
                            <v-list-item-title v-text="child.title"> </v-list-item-title>
                          </v-list-item-content>
                          <v-list-item-icon>
                            <v-btn @click="addToExploredCourses(child)" v-if= "child.selected == false">
                              <v-icon>
                                add
                              </v-icon>
                            </v-btn>
                            <v-icon v-if= "child.selected == true">
                              done
                            </v-icon>
                          </v-list-item-icon>

                        </v-list-item>
                      </v-list-group>
                    </v-list>
                </v-card>
            </v-col>
            </v-row>
      </v-container>

      <v-tooltip top v-if="exploredCourses.length != 0">
        <template v-slot:activator="{ on, attrs }">
          <v-btn large dark fixed bottom right v-bind="attrs" v-on="on" id= "computeBtn" @click="computePathways()" :to="{name: 'result'}" color= "#c65353" class="mt-9 mb-9 stickyButton">
            Compute Pathways
          </v-btn>
        </template>
        <span>Get all pathway layouts using the courses you've added to the list</span>
      </v-tooltip>

      <v-btn large disabled fixed bottom right id= "computeBtn" @click="computePathways()" v-if="exploredCourses.length == 0" color= "#c65353" class="mt-9 mb-9 stickyButton">
        Compute Pathways
      </v-btn>

    <div class="mt-5"></div>
  </div>
  
</template>

<script>

export default {
  props: ['path'],
  data() {
    return {
      exploredCourses: [/*{
          course: 'test',
        }*/],
      prefixes: [
        {
          title: 'ARTS',
          courses: [
            { title: '2500 –– History of Western Music', selected: false },
            { title: '2540 –– The Multimedia Century', selected: false },
            { title: '4130 –– New Media Theory', selected: false },
            { title: 'etc', selected: false },
          ]
        },
        {
          title: 'COGS',
          courses: [
            { title: '4410 –– Programming for Cognitive Science and Artificial Intelligence', selected: false },
            { title: '4420 –– Game AI', selected: false },
            { title: 'etc', selected: false },
          ]
        },
        {
          title: 'IHSS',
          courses: [
            { title: '~content~', selected: false }
          ]
        },
        {
          title: 'LANG',
          courses: [
            { title: '~content~', selected: false }
          ]
        },
        {
          title: 'PSYC',
          courses: [
            { title: '~content~', selected: false }
          ]
        },
        {
          title: 'STSH',
          courses: [
            { title: '~content~', selected: false }
          ],
        },
        {
          title: 'STSS',
          courses: [
            { title: '~content~', selected: false }
          ]
        },
      ]
    }
  },
  methods: {
    addToExploredCourses(course){
      /*let course = {
        "title" : courseTitle
      }*/
      course.selected = true;
      this.exploredCourses.push(course);
    },
    computePathways(){
      // will run when Compute Pathways button is pressed
    },
    filteredPrefixes() {
      return [] // will return all courses filtered based on prefix (IHSS, COGS, etc)
    },
    removeFromExploredCourses(index){
      this.exploredCourses[index].selected = false;
      this.exploredCourses.splice(index, 1);
    },
  },
  computed: {
  }
}

</script>

