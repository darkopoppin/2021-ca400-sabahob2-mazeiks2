<template>
  <ion-page>
      <h3>Welcome</h3>
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
  </ion-page>
</template>

<script>
import {
  IonPage,
  IonButton,
  IonContent
} from "@ionic/vue";
import { defineComponent } from "vue";
import { auth } from "../firebase";

export default defineComponent({
  name: "Home",
  components: {
    // IonContent,
    // IonHeader,
    IonPage,
    IonButton,
    IonContent
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
    redirect() {
      this.$router.push('/categorySelection')
    },
    recommender() {
      this.$router.push("/planner")
    },
  },
});
</script>