<template>
  <ion-page v-if="isMobile()">
      <ion-tabs>
      <ion-tab-bar slot="bottom">
        <ion-tab-button tab="category" href="/categories">
          <ion-icon :icon="list"></ion-icon>
          <ion-label>Categories</ion-label>
        </ion-tab-button>

        <ion-tab-button tab="planner" href="/mobilePlanner">
          <ion-icon :icon="calendar"></ion-icon>
          <ion-label>Planner</ion-label>
        </ion-tab-button>

        <ion-tab-button tab="settings" href="/mobileSettings">
          <ion-icon :icon="settings"></ion-icon>
          <ion-label>Settings</ion-label>
        </ion-tab-button>
      </ion-tab-bar>
    </ion-tabs>
  </ion-page>
  
  <ion-page v-else>
      <h3>Welcome to Desktop!</h3>
      <ion-content v-if="loggedIn"> {{user.displayName}}</ion-content>
      <ion-button @click="redirect" >Category selection</ion-button>
      <ion-button
        type="submit"
        v-on:click="recommender()"
      >
        plan me a day!
      </ion-button>
      <ion-button
        type="submit"
        v-on:click="logOut()"
      >
        Log out
      </ion-button>

      <ion-button @click="recommend">Recommend</ion-button>
  </ion-page>
</template>

<script>
import {
  IonPage,
  IonButton,
  IonContent,
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
    IonContent,
    IonPage,
    IonButton,
    IonTabBar, 
    IonTabButton, 
    IonTabs,
    IonIcon,
    IonLabel
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
      this.$router.push("/SignIn");
        auth
        .signOut()
        .then(() => {
          auth.onAuthStateChanged(() => {
            // this.$router.push("/");
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
