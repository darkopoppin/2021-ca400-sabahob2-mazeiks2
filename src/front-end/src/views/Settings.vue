<template>
  <ion-page>
      <ion-header>
        <ion-title size="small" class="component-title"> User Settings </ion-title>
      </ion-header>
    <ion-content>
      <ion-button type="submit" v-on:click="logOut()"> Log out </ion-button>
    </ion-content>
  </ion-page>
</template>

<script>
import {
  IonContent,
  IonHeader,
  IonPage,
  IonButton,
  IonTitle,
} from "@ionic/vue";
import { defineComponent } from "vue";
import { auth } from "../firebase";

export default defineComponent({
  name: "Settings",
  components: {
    IonContent,
    IonHeader,
    IonPage,
    IonButton,
    IonTitle,
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

<style>
.component-title {
  background-color: white;
  color: black;
  text-align: center;
  font-size: x-large;
}
</style>