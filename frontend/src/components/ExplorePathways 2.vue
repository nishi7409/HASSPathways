<template>
  <div>
    <span outlined class="pl-5 pt-8 headline font-weight-black"> Explore Pathways </span>

    <v-row class="mt-6" no-gutters>
      <v-col sm="5" md="6">
        <v-card class="pa-2" outlined tile>
          Selected Courses List
        </v-card>
      </v-col>
      <v-col sm="5" offset-sm="2" md="6" offset-md="0">
        <v-card class="pa-2" outlined tile>
          <!-- .col-sm-5 .offset-sm-2 .col-md-6 .offset-md-0 -->

          <v-expansion-panels v-model="panel" flat outlined tile accordion hover multiple class="pb-9 expansion-panel overflow-y-auto">
            <v-expansion-panel>
                <v-expansion-panel-header color="#c65353" id="expansion-header">
                Test
                </v-expansion-panel-header>

                <v-divider color="white"></v-divider>

            </v-expansion-panel>
            
            </v-expansion-panels>
            
        </v-card>
      </v-col>
    </v-row>

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
