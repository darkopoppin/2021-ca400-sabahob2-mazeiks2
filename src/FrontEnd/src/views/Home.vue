<template>
  <ion-page>
      <h3>Welcome</h3>
      <ion-content v-if="loggedIn"> {{user.displayName}}</ion-content>

      <ion-button @click="redirect" >Category selection</ion-button>
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
import firebase from "firebase/app";

export default defineComponent({
  name: "Home",
  components: {
    IonContent,
    // IonHeader,
    IonPage,
    IonButton,
  },
  data() {
    return {
      user: null,
      loggedIn: false,
    };
  },
  created() {
    firebase.auth().onAuthStateChanged((user) => {
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
      this.$router.push("/");
      firebase
        .auth()
        .signOut()
        .then(() => {
          firebase.auth().onAuthStateChanged(() => {
            // this.$router.push("/");
          });
        });
    },
    redirect() {
      this.$router.push('/categorySelection')
    },
  },
});
</script>