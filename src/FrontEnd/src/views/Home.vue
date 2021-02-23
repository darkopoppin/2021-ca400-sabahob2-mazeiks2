<template>
  <ion-page>
      <h3>Welcome</h3>
      <p>{{ user }}</p>

      <ion-button @click="() => this.$router.push('/categorySelection')" >Category selection</ion-button>
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
  IonContent,
  IonHeader,
  IonPage,
  IonTitle,
  IonToolbar,
  IonButton,
} from "@ionic/vue";
import { defineComponent } from "vue";
import firebase from "firebase";

export default defineComponent({
  name: "Home",
  components: {
    // IonContent,
    // IonHeader,
    IonPage,
    IonButton,
    // IonTitle,
    // IonToolbar
  },
  data() {
    return {
      user: null,
    };
  },
  created() {
    firebase.auth().onAuthStateChanged((user) => {
      if (user) {
        this.user = user;
      } else {
        this.user = null;
      }
    });
  },
  methods: {
    logOut() {
      firebase
        .auth()
        .signOut()
        .then(() => {
          firebase.auth().onAuthStateChanged(() => {
            this.$router.push("/");
          });
        });
    },
  },
});
</script>