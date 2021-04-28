<template>
  <ion-page>
      <ion-tabs>
      <ion-tab-bar v-if="isMobile()" slot="bottom">
        <ion-tab-button tab="category" href="/Categories">
          <ion-icon :icon="list"></ion-icon>
          <ion-label>Categories</ion-label>
        </ion-tab-button>

        <ion-tab-button tab="planner" href="/Planner">
          <ion-icon :icon="calendar"></ion-icon>
          <ion-label>Planner</ion-label>
        </ion-tab-button>

        <ion-tab-button tab="settings" href="/Settings">
          <ion-icon :icon="settings"></ion-icon>
          <ion-label>Settings</ion-label>
        </ion-tab-button>
      </ion-tab-bar>

      <ion-tab-bar v-else slot="top">
        <ion-title class="title">Welcome to CiteCy!</ion-title>
        <ion-tab-button tab="category" href="/Categories">
          <ion-icon :icon="list"></ion-icon>
          <ion-label>Categories</ion-label>
        </ion-tab-button>

        <ion-tab-button tab="planner" href="/Planner">
          <ion-icon :icon="calendar"></ion-icon>
          <ion-label>Planner</ion-label>
        </ion-tab-button>

        <ion-tab-button tab="settings" href="/Settings">
          <ion-icon :icon="settings"></ion-icon>
          <ion-label>Settings</ion-label>
        </ion-tab-button>
      </ion-tab-bar>
    </ion-tabs>
  </ion-page>
  
</template>

<script>
import {
  IonPage,
  IonTitle,
  IonTabBar, 
  IonTabButton, 
  IonTabs,
  IonIcon,
  IonLabel,
} from "@ionic/vue";
import { defineComponent } from "vue";
import { auth } from "../firebase";
import axios from "axios";
import { list, calendar, settings } from 'ionicons/icons';

export default defineComponent({
  name: "Home",
  components: {
    IonPage,
    IonTitle,
    IonTabBar, 
    IonTabButton, 
    IonTabs,
    IonIcon,
    IonLabel,
  },
  setup() {
    return {
        list,
        calendar,
        settings
        }
  },
  data() {
    return {
      user: null,
      loggedIn: false,
    };
  },
  created() {
    auth.onAuthStateChanged((user) => {
      if (user) {
        this.user = user;
        this.loggedIn = true;
      } else {
        this.user = null;
        this.loggedIn = false;
      }
    });
  },
  methods: {
    logOut() {
        auth
        .signOut()
        .then(() => {
          auth.onAuthStateChanged(() => {
            this.$router.push("/SignIn");
          });
        });
    },
    isMobile() {
        if( screen.width <= 760 ) {
            return true;
        }
        else {
            return false;
        }
    },
    redirect() {
      this.$router.push('/categorySelection')
    },
    recommender() {
      this.$router.push("/planner")
    },
    recommend(){
      axios.get('http://127.0.0.1:5000/recommender', 
      { params: {'user_id': 'KbcIgBXo6bhtfRtO6iWe'} })
      .then(response => console
      .log(response))
      .catch(error => console.log(error))
    }
  },
});
</script>

<style scoped>
.title {
    text-align: left;
}

</style>