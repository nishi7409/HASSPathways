<template>
  <div>
      
    <v-container fill-height>
        <span outlined class="pt-8 headline font-weight-black"> Explore Pathways </span>
          <!-- <v-row justify="center" align="center" class= "pt-10"> -->
        <v-row class= "pt-7">
            <v-col cols="6" md="4">

              <v-list light outlined v-if="exploredCourses.length != 0"> 
                <v-list-item>
                  <v-list-item-content>
                    <v-list-item-title>
                      A course...
                    </v-list-item-title>
                  </v-list-item-content>
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
                      <v-list-group v-for="item in items" :key="item.title" v-model="item.active" :prepend-icon="item.action" no-action>
                        <template v-slot:activator>
                          <v-list-item-content>
                            <v-list-item-title v-text="item.title" class= "ml-10">
                            </v-list-item-title>
                          </v-list-item-content>
                        </template>

                        <v-list-item v-for="child in item.items" :key="child.title">
                          <v-list-item-content>
                            <v-list-item-title v-text="child.title">
                              Test
                            </v-list-item-title>
                          </v-list-item-content>
                          <v-list-item-icon>
                            <v-btn>
                              <v-icon>
                                mdi-plus-circle
                              </v-icon>
                            </v-btn>
                          </v-list-item-icon>

                        </v-list-item>
                      </v-list-group>
                    </v-list>
                </v-card>
            </v-col>
            </v-row>
      </v-container>
    <v-btn large dark fixed bottom right id= "computeBtn" @click="computePathways()" v-if="exploredCourses.length != 0" color= "#c65353" class="mt-9 mb-9 stickyButton">
        Compute Pathways
    </v-btn>

    <v-btn large disabled fixed bottom right id= "computeBtn" @click="computePathways()" v-if="exploredCourses.length == 0" color= "#c65353" class="mt-9 mb-9 stickyButton">
        Compute Pathways
    </v-btn>
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
      items: [
        {
          items: [
            { title: '2500 –– History of Western Music' },
            { title: '2540 –– The Multimedia Century' },
            { title: '4130 –– New Media Theory' },
            { title: 'etc' },
          ],
          title: 'ARTS',
        },
        {
          active: true,
          items: [
            { title: '4410 –– Programming for Cognitive Science and Artificial Intelligence' },
            { title: '4420 –– Game AI' },
            { title: 'etc' },
          ],
          title: 'COGS',
        },
        {
          items: [{ title: '~content~' }],
          title: 'IHSS',
        },
        {
          items: [{ title: '~content~' }],
          title: 'LANG',
        },
        {
          items: [{ title: '~content~' }],
          title: 'PSYC',
        },
        {
          items: [{ title: '~content~' }],
          title: 'STSH',
        },
        {
          items: [{ title: '~content~' }],
          title: 'STSS',
        },
      ]
    }
  },
  methods: {
    computePathways(){
      // will run when Compute Pathways button is pressed
    },
    filteredPrefixes() {
      return [] // will return all courses filtered based on prefix (IHSS, COGS, etc)
    }
  },
  computed: {
  }
}

</script>

