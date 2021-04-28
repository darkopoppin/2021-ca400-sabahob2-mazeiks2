<template>
  <ion-page>
    <ion-content>
      <ion-header>User settings</ion-header>
      <ion-button type="submit" v-on:click="logOut()"> Log out </ion-button>
    </ion-content>
  </ion-page>
</template>

<script>
import { IonContent, IonHeader, IonPage } from "@ionic/vue";
import { defineComponent } from "vue";
import { auth } from "../firebase";

export default defineComponent({
  name: "Settings",
  components: {
    IonContent,
    IonHeader,
    IonPage,
  },
  methods: {
    logOut() {
      auth.signOut().then(() => {
        auth.onAuthStateChanged(() => {
          this.$router.push("/SignIn");
        });
      });
    },
  },
});
</script>