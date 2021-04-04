<template>
  <ion-page>
    <h3>Welcome</h3>
    <p>{{ user }}</p>

    <ion-button type="submit" v-on:click="logOut()"> Log out </ion-button>
  </ion-page>
</template>

<script>
import { IonPage, IonButton } from "@ionic/vue";
import { defineComponent } from "vue";
import firebase from "firebase/app";

export default defineComponent({
  name: "Home",
  components: {
    IonPage,
    IonButton,
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