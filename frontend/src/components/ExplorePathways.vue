<template>
  <div>
      
    <v-container fill-height>
        <span outlined class="pl-5 pt-8 headline font-weight-black"> Explore Pathways </span>
          <!-- <v-row justify="center" align="center" class= "pt-10"> -->
        <v-row justify="center" class= "pt-5">
            <v-col cols="6" md="4" class="ml-6">
                <v-card class="pa-2" outlined tile>
                Selected Courses List
                </v-card>
            </v-col>

            <v-col cols="12" md="7" class="ml-6">
                <v-card class="pa-2" outlined tile>
                <!-- .col-12 .col-md-8 -->

                <v-expansion-panels v-model="panel" flat outlined tile accordion hover multiple class="pb-9 expansion-panel overflow-y-auto">
                    <v-expansion-panel>
                        <v-expansion-panel-header color="#c65353" id="expansion-header">
                        Test Panel
                        </v-expansion-panel-header>

                        <v-divider color="white"></v-divider>

                    </v-expansion-panel>
                    
                    </v-expansion-panels>
                </v-card>
            </v-col>
            </v-row>
      </v-container>



    <v-col class="text-left">
        test
    </v-col>




    <v-list>
        test
        test
        test
    </v-list>




  </div>
</template>
